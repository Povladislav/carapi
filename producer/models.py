from django.db import models
from django.utils import timezone


class Producer(models.Model):
    title = models.CharField(max_length=50)
    year_of_establishment = models.DateTimeField()
    buyers = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    available_cars = models.ForeignKey('car.Car', on_delete=models.CASCADE, related_name='available_cars')
    sold_cars = models.ForeignKey('car.Car', on_delete=models.CASCADE, related_name='sold_cars')
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
