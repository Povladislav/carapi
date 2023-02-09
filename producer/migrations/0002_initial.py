# Generated by Django 4.1.6 on 2023-02-09 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0003_delete_carsell'),
        ('producer', '0001_initial'),
        ('showroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producer',
            name='available_cars',
            field=models.ManyToManyField(blank=True, related_name='available_cars_for_showroom', to='showroom.availablecar'),
        ),
        migrations.AddField(
            model_name='producer',
            name='discount',
            field=models.ManyToManyField(blank=True, related_name='discount_for_showroom', to='showroom.discount'),
        ),
        migrations.AddField(
            model_name='producer',
            name='history',
            field=models.ManyToManyField(related_name='history_of_producer', to='producer.history'),
        ),
        migrations.AddField(
            model_name='history',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='showroom_buyer', to='showroom.showroom'),
        ),
        migrations.AddField(
            model_name='history',
            name='sold_car',
            field=models.ManyToManyField(related_name='sold_car_for_showroom', to='car.car'),
        ),
    ]
