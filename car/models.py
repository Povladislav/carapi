from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class Car(models.Model):
    class MODELS(models.TextChoices):
        Audi = 'audi'
        BMW = 'bmw'
        MERCEDES = 'mercedes'
        LEXUS = 'lexus'

    class COLORS(models.TextChoices):
        BLACK = 'black'
        RED = 'red'
        YELLOW = 'yellow'
        GREEN = 'green'

    class POWER(models.TextChoices):
        POWER1 = 120
        POWER2 = 200
        POWER3 = 350
        POWER4 = 420

    model = models.CharField(choices=MODELS.choices, max_length=15, blank=True)
    color = models.CharField(choices=COLORS.choices, max_length=15, blank=True)
    power = models.CharField(choices=POWER.choices, max_length=15, blank=True)
    price = models.SmallIntegerField(validators=[MinValueValidator(0)], blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
