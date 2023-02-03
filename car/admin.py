from django.contrib import admin

from car.models import Car, Color, ModelName

admin.site.register([Car, ModelName, Color])
