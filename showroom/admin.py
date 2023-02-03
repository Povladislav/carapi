from django.contrib import admin

from showroom.models import SalesForCustomer, ShowRoom

admin.site.register([ShowRoom, SalesForCustomer])
