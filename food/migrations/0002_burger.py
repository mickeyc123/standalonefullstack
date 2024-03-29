# Generated by Django 5.0.3 on 2024-03-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price_m', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Price (Medium)')),
                ('price_l', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Price (Large)')),
                ('imageb', models.ImageField(blank=True, null=True, upload_to='pizza_images/', verbose_name='Pizza Image')),
            ],
        ),
    ]