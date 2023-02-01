# Generated by Django 4.1.5 on 2023-02-01 08:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car_created_at_car_is_active_car_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
