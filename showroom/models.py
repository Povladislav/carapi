from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator


class ShowRoom(models.Model):
    title = models.CharField(max_length=50)
    country = CountryField()
    balance = models.IntegerField(validators=[MinValueValidator(0)])
    buyers = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    sold_cars = models.ForeignKey('car.Car', on_delete=models.CASCADE, related_name='sold_for_customer_cars')
    cars_to_sell = models.ForeignKey('car.Car', on_delete=models.CASCADE, related_name='cars_to_sell')
    preferable_cars = models.ForeignKey('car.Car', on_delete=models.CASCADE, related_name='preferable_cars')
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
