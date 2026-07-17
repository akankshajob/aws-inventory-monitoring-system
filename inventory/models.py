from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Latex', 'Latex Examination Gloves'),
        ('Nitrile', 'Nitrile Examination Gloves'),
        ('Cleanroom', 'Cleanroom Gloves'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('Normal', 'Normal'),
        ('Low', 'Low'),
        ('Critical', 'Critical'),
        ('Out of Stock', 'Out of Stock'),
    ]

    product_name     = models.CharField(max_length=100)
    category         = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    current_quantity = models.IntegerField(default=0)
    min_threshold    = models.IntegerField()
    unit             = models.CharField(max_length=20, default='boxes')
    last_updated     = models.DateTimeField(auto_now=True)
    updated_by       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def is_below_threshold(self):
        return self.current_quantity < self.min_threshold

    def get_stock_status(self):
        if self.current_quantity == 0:
            return 'Out of Stock'
        elif self.current_quantity < self.min_threshold:
            return 'Critical'
        elif self.current_quantity < self.min_threshold * 1.5:
            return 'Low'
        return 'Normal'

    def __str__(self):
        return self.product_name


class StockTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('add', 'Add Stock'),
        ('deduct', 'Deduct Stock'),
        ('update', 'Update Stock'),
    ]
    product          = models.ForeignKey(Product, on_delete=models.CASCADE)
    user             = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    quantity_changed = models.IntegerField()
    quantity_after   = models.IntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    remarks          = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.product_name} - {self.transaction_type}"


class AlertLog(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('failed', 'Failed'),
        ('pending', 'Pending'),
    ]
    product            = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_at_alert  = models.IntegerField()
    threshold_at_alert = models.IntegerField()
    alert_message      = models.TextField()
    triggered_at       = models.DateTimeField(auto_now_add=True)
    alert_status       = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    sent_to_email      = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"Alert: {self.product.product_name} - {self.triggered_at}"
