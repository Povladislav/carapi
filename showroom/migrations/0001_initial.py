# Generated by Django 4.1.6 on 2023-02-13 09:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date_of_start', models.DateField()),
                ('date_of_end', models.DateField()),
                ('size', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('count', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('whole_price', models.DecimalField(decimal_places=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('buyer_customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShowRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('balance', models.DecimalField(decimal_places=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)])),
                ('year_of_establishment', models.DateTimeField()),
                ('discount', models.ManyToManyField(blank=True, related_name='discount_for_customer', to='showroom.discount')),
                ('history', models.ManyToManyField(blank=True, related_name='history_of_sells', to='showroom.history')),
                ('preferable_cars', models.ManyToManyField(blank=True, related_name='preferable_cars', to='car.preferablecar')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='history',
            name='buyer_showroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_showroom', to='showroom.showroom'),
        ),
        migrations.AddField(
            model_name='history',
            name='sold_car',
            field=models.ManyToManyField(related_name='sold_car', to='car.car'),
        ),
    ]
