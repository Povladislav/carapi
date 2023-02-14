# Generated by Django 4.1.6 on 2023-02-14 09:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=15)),
                ('power', models.CharField(blank=True, choices=[('120', 'Horses120'), ('200', 'Horses200'), ('350', 'Horses350'), ('420', 'Horses420')], max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PreferableCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=6)),
                ('count', models.DecimalField(decimal_places=0, max_digits=2)),
                ('preferable_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.color'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.modelname'),
        ),
        migrations.CreateModel(
            name='AvailableCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('count', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('price', models.DecimalField(decimal_places=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('available_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
