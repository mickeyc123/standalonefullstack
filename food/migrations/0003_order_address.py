# Generated by Django 4.2.11 on 2024-04-05 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_remove_order_address_remove_order_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
    ]
