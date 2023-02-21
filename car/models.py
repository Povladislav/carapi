from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from customer.models import DateMixin, IsActiveMixin


class Car(DateMixin, IsActiveMixin):
    class POWER(models.TextChoices):
        HORSES120 = 120
        HORSES200 = 200
        HORSES350 = 350
        HORSES420 = 420

    name = models.CharField(max_length=15)
    model = models.ForeignKey('ModelName', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    power = models.CharField(choices=POWER.choices, max_length=15, blank=True)

    def __str__(self):
        return self.name


class AvailableCar(IsActiveMixin, DateMixin):
    available_car = models.ForeignKey('car.Car', on_delete=models.CASCADE)
    count = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    showroom = models.ForeignKey('showroom.ShowRoom', on_delete=models.CASCADE,
                                 related_name='available_cars_for_showroom',
                                 null=True, blank=True)
    producer = models.ForeignKey('producer.Producer', on_delete=models.CASCADE,
                                 related_name='available_cars_for_producer', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=0, validators=[MinValueValidator(0)])
    discount = models.ForeignKey('showroom.Discount', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.available_car.name


class PreferableCar(IsActiveMixin, DateMixin):
    preferable_car = models.ForeignKey('car.Car', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    count = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.preferable_car.name


class ModelName(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
