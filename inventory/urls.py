from django.urls import path
from . import views

urlpatterns = [
    path('',              views.login_view,    name='login'),
    path('logout/',       views.logout_view,   name='logout'),
    path('dashboard/',    views.dashboard,     name='dashboard'),
    path('products/',     views.product_list,  name='product_list'),
    path('add/',          views.add_product,   name='add_product'),
    path('update/<int:product_id>/', views.update_stock,   name='update_stock'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('alerts/',       views.alert_history, name='alert_history'),
]