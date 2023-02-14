from django.contrib import admin

from customer.models import Location, User

admin.site.register([User, Location])
