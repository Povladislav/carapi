# Generated by Django 4.1.6 on 2023-02-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_car_sold_to_customer_car_sold_to_showroom'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='purchased_cars',
            field=models.ManyToManyField(blank=True, to='car.car'),
        ),
    ]
