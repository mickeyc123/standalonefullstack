from django.db import models
from django.utils import timezone


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_m = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Price (Medium)')
    price_l = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Price (Large)')
    image = models.ImageField(upload_to='pizza_images/', null=True, blank=True, verbose_name='Pizza Image')

    def __str__(self):
        return self.name

class Burger(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_m = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Price (Medium)')
    price_l = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='Price (Large)')
    imageb = models.ImageField(upload_to='burger_images/', null=True, blank=True, verbose_name='Burger Image')

    def __str__(self):
        return self.name



class Order(models.Model):
    note = models.TextField()
    orders = models.JSONField(default=list)  # Default is an empty list
    created_at = models.DateTimeField(default=timezone.now)  # Default is current time
    address = models.CharField(max_length=255, default="")  # Default is empty string

    def __str__(self):
        return f"Order {self.id}"

