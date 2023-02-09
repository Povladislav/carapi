# Generated by Django 4.1.6 on 2023-02-09 09:59

import django.core.validators
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('balance', models.DecimalField(decimal_places=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)])),
                ('year_of_establishment', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
