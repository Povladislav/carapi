from django.contrib import admin

from showroom.models import Discount, History, ShowRoom

admin.site.register([ShowRoom, History, Discount])
