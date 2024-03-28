
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Pizza,Burger

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_m', 'price_l', 'image_preview']
    search_fields = ['name']
    list_filter = ['price_m', 'price_l']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{url}" width="100" />'.format(url=obj.image.url))
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
            return mark_safe('<img src="{url}" width="100" />'.format(url=obj.imageb.url))
        else:
            return 'No Image'
    
    image_preview.short_description = 'Image Preview'
