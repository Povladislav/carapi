# Generated by Django 4.1.6 on 2023-02-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_user_is_verified_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=44, unique=True),
        ),
    ]
