from django.core.validators import MinValueValidator
from django.db import models

from customer.models import DateMixin, IsActiveMixin


class Producer(IsActiveMixin, DateMixin):
    title = models.CharField(max_length=50)
    year_of_establishment = models.DateTimeField()
    buyers = models.ManyToManyField('showroom.ShowRoom', blank=True)
    available_cars = models.ManyToManyField('car.Car', related_name='available_cars')
    sold_cars = models.ManyToManyField('car.Car', related_name='sold_cars', blank=True)

    def __str__(self):
        return self.title


class SalesForShowRoom(IsActiveMixin, DateMixin):
    date_of_start = models.DateField()
    discount_size = models.DecimalField(validators=[MinValueValidator(0)], decimal_places=0, max_digits=6, blank=True)
    date_of_end = models.DateField()
    cars_on_sales = models.ManyToManyField('car.Car',
                                           limit_choices_to={'sold_to_customer': False, 'sold_to_showroom': False})

    def __str__(self):
        return f'SaleForShowRoom{self.id}'
