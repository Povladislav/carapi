from django.core.validators import MinValueValidator
from django.db import models


class Customer(models.Model):
    balance = models.SmallIntegerField(validators=[MinValueValidator(0)])
    info = models.CharField(max_length=200)
    purchased_cars = models.ForeignKey('car.Car', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
