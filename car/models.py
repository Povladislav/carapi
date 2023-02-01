from django.core.validators import MinValueValidator
from django.db import models

from customer.models import DateMixin, IsActiveMixin


class Car(DateMixin, IsActiveMixin):
    class POWER(models.TextChoices):
        HORSES120 = 120
        HORSES200 = 200
        HORSES350 = 350
        HORSES420 = 420

    model = models.ForeignKey('Model', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    power = models.CharField(choices=POWER.choices, max_length=15, blank=True)
    price = models.DecimalField(validators=[MinValueValidator(0)], blank=True, decimal_places=0, max_digits=6)


class Model(models.Model):
    title = models.CharField(max_length=50)


class Color(models.Model):
    title = models.CharField(max_length=50)
