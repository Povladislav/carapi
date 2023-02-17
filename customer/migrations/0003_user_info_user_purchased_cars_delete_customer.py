# Generated by Django 4.1.6 on 2023-02-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_initial'),
        ('customer', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='info',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='purchased_cars',
            field=models.ManyToManyField(blank=True, to='car.car'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
