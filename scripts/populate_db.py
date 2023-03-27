import os
import random

import django
from django.conf import settings
from django.db import connection
from django_countries import countries

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

django.setup()
from car.models import AvailableCar, Car, Color, ModelName
from customer.models import Location
from producer.models import Producer
from showroom.models import ShowRoom

# cars = {
#     "model": random.choice(ModelName.objects.all()),
#     "color": random.choice(Color.objects.all()),
#     "power": random.choice(Car.POWER.choices)[0]
# }


def populate_cars():
    for i in range(20):
        cars = {
            "model": random.choice(ModelName.objects.all()),
            "color": random.choice(Color.objects.all()),
            "power": random.choice(Car.POWER.choices)[0]
        }
        Car.objects.create(**cars)


def populate_with_sql():
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO car_color(title) VALUES('BLUE'),('GREY'),('RED'),('MAGENTA'),('BLACK'),('GREEN')")
        cursor.execute(
            "INSERT INTO car_modelname(title) VALUES('AUDIA4'),('AUDIA6'),('MAZDA3'),('MAZDA5'),('HYUNDAY_Sonata'),('VW_Polo'),('VW_Passat'),('BMWX5'),('BMW3')")


def populate_with_locations():
    for i in range(20):
        location = {
            "country": random.choice(countries)[0]
        }
        Location.objects.create(**location)


def populate_with_showrooms():
    titles = ["SR441", "SR545", "SR8871", "SR8999", "SR0912"]
    dates = ["1981-04-21 11:23:24", "1999-07-04 22:11:24", "2011-09-09 01:02:23", "1987-11-22 14:11:27",
             "2000-06-11 11:23:44"]
    for i in range(len(titles)):
        showroom = {
            "title": titles[i],
            "country": random.choice(Location.objects.all()),
            "balance": random.randint(300000, 999000),
            "year_of_establishment": dates[i]
        }
        ShowRoom.objects.create(**showroom)


def populate_with_producers():
    titles = ["PROD441", "PROD545", "PROD8871", "PROD8999", "PROD0912"]
    dates = ["1989-04-21 11:23:24", "1979-07-04 22:11:24", "2021-09-09 01:02:23", "1987-11-22 14:11:27",
             "2000-06-11 11:23:44"]
    for i in range(len(titles)):
        producer = {
            "title": titles[i],
            "country": random.choice(Location.objects.all()),
            "year_of_establishment": dates[i]
        }
        Producer.objects.create(**producer)


def populate_with_av_cars():
    for i in range(len(ShowRoom.objects.all())):
        av_car_for_showroom = {
            "available_car": random.choice(Car.objects.all()),
            "count": random.randint(1, 20),
            "showroom": random.choice(ShowRoom.objects.all()),
            "price": random.randint(30000, 99000)
        }
        AvailableCar.objects.create(**av_car_for_showroom)
    for i in range(len(Producer.objects.all())):
        av_car_for_producer = {
            "available_car": random.choice(Car.objects.all()),
            "count": random.randint(1, 20),
            "producer": random.choice(Producer.objects.all()),
            "price": random.randint(20000, 79000)
        }
        AvailableCar.objects.create(**av_car_for_producer)

#
# populate_with_sql()
# populate_cars()
# populate_with_locations()
# populate_with_showrooms()
# populate_with_producers()
# populate_with_av_cars()
