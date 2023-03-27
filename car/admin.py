from django.contrib import admin

from car.models import AvailableCar, Car, Color, ModelName, PreferableCar

admin.site.register([Car, ModelName, Color, AvailableCar, PreferableCar])
