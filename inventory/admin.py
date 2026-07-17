from django.contrib import admin
from .models import Product, StockTransaction, AlertLog

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ['product_name', 'category', 'current_quantity', 'min_threshold', 'get_stock_status', 'last_updated']
    list_filter   = ['category']
    search_fields = ['product_name']

@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = ['product', 'transaction_type', 'quantity_changed', 'quantity_after', 'transaction_date']

@admin.register(AlertLog)
class AlertLogAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity_at_alert', 'threshold_at_alert', 'alert_status', 'triggered_at']