# Generated by Django 4.1.6 on 2023-02-14 09:18

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('balance', models.DecimalField(decimal_places=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('info', models.CharField(max_length=200)),
                ('purchased_cars', models.ManyToManyField(blank=True, to='car.car')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
