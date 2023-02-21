from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from car.models import Car
from customer.models import DateMixin, IsActiveMixin, Location


class ShowRoom(IsActiveMixin, DateMixin):
    title = models.CharField(max_length=50, unique=True)
    country = models.ForeignKey(Location, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=8, decimal_places=0, validators=[MinValueValidator(0)])
    year_of_establishment = models.DateTimeField()
    preferable_cars = models.ManyToManyField('car.PreferableCar', related_name='preferable_cars', blank=True)
    history = models.ManyToManyField('History', related_name='history_of_sells', blank=True)
    discount = models.ManyToManyField('Discount', related_name='discount_for_customer', blank=True)

    def __str__(self):
        return self.title


class History(IsActiveMixin, DateMixin):
    buyer_customer = models.ForeignKey('customer.User', on_delete=models.CASCADE, related_name='buyer_customer',
                                       null=True, blank=True)
    buyer_showroom = models.ForeignKey('showroom.ShowRoom', on_delete=models.CASCADE, related_name='buyer_showroom',
                                       null=True, blank=True)
    count = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    whole_price = models.DecimalField(max_digits=6, decimal_places=0, validators=[MinValueValidator(0)])
    sold_car = models.ManyToManyField('car.Car', related_name='sold_car')

    def __str__(self):
        return f'History{self.id}'


class Discount(IsActiveMixin, DateMixin):
    car = models.ForeignKey('car.Car', on_delete=models.CASCADE)
    date_of_start = models.DateField(default=timezone.now)
    date_of_end = models.DateField(default=timezone.now)
    size = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(1)])

    def __str__(self):
        return f'Discount{self.id}'
