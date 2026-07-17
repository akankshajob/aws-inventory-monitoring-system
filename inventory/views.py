from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, StockTransaction, AlertLog

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'inventory/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    products = Product.objects.all()
    statuses = [p.get_stock_status() for p in products]
    context = {
        'products':       products,
        'total':          products.count(),
        'normal_count':   statuses.count('Normal'),
        'low_count':      statuses.count('Low'),
        'critical_count': statuses.count('Critical') + statuses.count('Out of Stock'),
    }
    return render(request, 'inventory/dashboard.html', context)

@login_required(login_url='login')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/dashboard.html', {
        'products': products,
        'total': products.count(),
        'normal_count': sum(1 for p in products if p.get_stock_status() == 'Normal'),
        'low_count': sum(1 for p in products if p.get_stock_status() == 'Low'),
        'critical_count': sum(1 for p in products if p.get_stock_status() in ['Critical', 'Out of Stock']),
    })

@login_required(login_url='login')
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Only Admin can add products.')
        return redirect('dashboard')
    if request.method == 'POST':
        Product.objects.create(
            product_name     = request.POST['product_name'],
            category         = request.POST['category'],
            current_quantity = int(request.POST['current_quantity']),
            min_threshold    = int(request.POST['min_threshold']),
            unit             = request.POST.get('unit', 'boxes'),
            updated_by       = request.user
        )
        messages.success(request, 'Product added successfully!')
        return redirect('dashboard')
    return render(request, 'inventory/add_product.html')

@login_required(login_url='login')
def update_stock(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        old_qty  = product.current_quantity
        new_qty  = int(request.POST['current_quantity'])
        diff     = new_qty - old_qty
        t_type   = 'add' if diff > 0 else 'deduct' if diff < 0 else 'update'

        product.current_quantity = new_qty
        product.min_threshold    = int(request.POST['min_threshold'])
        product.updated_by       = request.user
        product.save()

        StockTransaction.objects.create(
            product          = product,
            user             = request.user,
            transaction_type = t_type,
            quantity_changed = abs(diff),
            quantity_after   = new_qty,
            remarks          = request.POST.get('remarks', '')
        )
        messages.success(request, f'Stock updated for {product.product_name}!')
        return redirect('dashboard')
    return render(request, 'inventory/update_stock.html', {'product': product})

@login_required(login_url='login')
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only Admin can delete products.')
        return redirect('dashboard')
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product deleted.')
    return redirect('dashboard')

@login_required(login_url='login')
def alert_history(request):
    alerts = AlertLog.objects.all().order_by('-triggered_at')
    return render(request, 'inventory/alert_history.html', {'alerts': alerts})