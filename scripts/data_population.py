import random

from django.db import connection

from car.models import Car, Color, ModelName

name = ["AUDIA4", "BMW3", "BMW5"]
cars = {
    "name": random.choice(name),
    "model_id": random.choice(ModelName.objects.all()),
    "color_id": random.choice(Color.objects.all()),
    "power": random.choice(Car.POWER.choices)
}


def foo():
    Car.objects.create(**cars)


#
# def populate_with_sql():
#     with connection.cursor() as cursor:
#         cursor.execute("INSERT INTO car_color(title) VALUES('BLUE'),('GREY'),('RED'),('MAGENTA'),('BLACK'),('GREEN')")
#         cursor.execute(
#             "INSERT INTO car_modelname(title) VALUES('A4'),('A6'),('3'),('5'),('Sonata'),('Polo'),('Passat')")

foo()
