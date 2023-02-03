from django.core.validators import MinValueValidator
from django.db import models
from django_countries.fields import CountryField

from car.models import Car
from customer.models import DateMixin, IsActiveMixin


class ShowRoom(IsActiveMixin, DateMixin):
    title = models.CharField(max_length=50)
    country = CountryField()
    balance = models.IntegerField(validators=[MinValueValidator(0)])
    buyers = models.ForeignKey('customer.Customer', on_delete=models.CASCADE, blank=True, null=True)
    sold_cars = models.ManyToManyField('car.Car', related_name='sold_for_customer_cars', blank=True)
    cars_to_sell = models.ManyToManyField('car.Car', related_name='cars_to_sell', blank=True)
    preferable_cars = models.ManyToManyField('car.Car', related_name='preferable_cars', blank=True)

    def __str__(self):
        return self.title


class SalesForCustomer(IsActiveMixin, DateMixin):
    date_of_start = models.DateField()
    discount_size = models.DecimalField(validators=[MinValueValidator(0)], decimal_places=0, max_digits=6, blank=True)
    date_of_end = models.DateField()
    cars_on_sales = models.ManyToManyField('car.Car',
                                           limit_choices_to={'sold_to_customer': False, 'sold_to_showroom': True})

    def __str__(self):
        return f'SaleForCustomer{self.id}'
