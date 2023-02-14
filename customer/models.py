from django.core.validators import MinValueValidator
from django.db import models
from django_countries.fields import CountryField


class DateMixin(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class IsActiveMixin(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Location(models.Model):
    country = CountryField()


class Customer(DateMixin, IsActiveMixin):
    balance = models.DecimalField(validators=[MinValueValidator(0)], decimal_places=0, max_digits=6)
    info = models.CharField(max_length=200)
    purchased_cars = models.ManyToManyField('car.Car', blank=True)

    def __str__(self):
        return f'Customer{self.id}'
