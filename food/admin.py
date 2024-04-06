from django.contrib import admin
from django.utils.html import mark_safe
from .models import Pizza, Burger, Order
import json

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_m', 'price_l', 'image_preview']
    search_fields = ['name']
    list_filter = ['price_m', 'price_l']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="100" />'.format(obj.image.url))
        else:
            return 'No Image'
    
    image_preview.short_description = 'Image Preview'

@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_m', 'price_l', 'image_preview']
    search_fields = ['name']
    list_filter = ['price_m', 'price_l']

    def image_preview(self, obj):
        if obj.imageb:
            return mark_safe('<img src="{}" width="100" />'.format(obj.imageb.url))
        else:
            return 'No Image'
    
    image_preview.short_description = 'Image Preview'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'note', 'get_orders', 'created_at', 'address']
    search_fields = ['note', 'address']
    list_filter = ['created_at']

    def get_orders(self, obj):
        # Custom method to display orders in a readable format
        try:
            orders_list = obj.orders
            orders_str = ", ".join([f"{order['item']} x{order['quantity']}" for order in orders_list])
            return orders_str
        except (TypeError, KeyError):
            return "Invalid Orders"

    get_orders.short_description = 'Orders'
