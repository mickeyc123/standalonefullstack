from django.db import models

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
    imageb = models.ImageField(upload_to='pizza_images/', null=True, blank=True, verbose_name='Burger Image')

    def __str__(self):
        return self.name
