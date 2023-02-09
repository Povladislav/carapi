from django.contrib import admin

from showroom.models import (AvailableCar, Discount, History, PreferableCar,
                             ShowRoom)

admin.site.register([ShowRoom, AvailableCar, PreferableCar, History, Discount])
