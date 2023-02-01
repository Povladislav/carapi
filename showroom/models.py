from django.core.validators import MinValueValidator
from django.db import models
from django_countries.fields import CountryField

from customer.models import DateMixin, IsActiveMixin


class ShowRoom(IsActiveMixin, DateMixin):
    title = models.CharField(max_length=50)
    country = CountryField()
    balance = models.IntegerField(validators=[MinValueValidator(0)])
    buyers = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    sold_cars = models.ManyToManyField('car.Car', related_name='sold_for_customer_cars')
    cars_to_sell = models.ManyToManyField('car.Car', related_name='cars_to_sell')
    preferable_cars = models.ManyToManyField('car.Car', related_name='preferable_cars')
