# Generated by Django 4.1.6 on 2023-02-17 09:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("showroom", "0002_showroom_available_cars"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="showroom",
            name="available_cars",
        ),
    ]
