# Generated by Django 4.1.6 on 2023-02-14 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('showroom', '0001_initial'),
        ('car', '0001_initial'),
        ('producer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='availablecar',
            name='producer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='available_cars_for_producer', to='producer.producer'),
        ),
        migrations.AddField(
            model_name='availablecar',
            name='showroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='available_cars_for_showroom', to='showroom.showroom'),
        ),
    ]