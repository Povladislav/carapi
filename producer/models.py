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