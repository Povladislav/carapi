from django.core.validators import MinValueValidator
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


class ModelName(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
