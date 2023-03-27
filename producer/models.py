from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from customer.models import DateMixin, IsActiveMixin, Location


class Producer(IsActiveMixin, DateMixin):
    title = models.CharField(max_length=50, unique=True)
    country = models.ForeignKey(Location, on_delete=models.CASCADE)
    year_of_establishment = models.DateTimeField()
    discount = models.ManyToManyField(
        "showroom.Discount", related_name="discount_for_showroom", blank=True
    )
    history = models.ManyToManyField(
        "History", related_name="history_of_producer", blank=True
    )

    def __str__(self):
        return self.title


class History(IsActiveMixin, DateMixin):
    buyer = models.ForeignKey(
        "showroom.ShowRoom", on_delete=models.CASCADE, related_name="showroom_buyer"
    )
    sold_car = models.ManyToManyField("car.Car", related_name="sold_car_for_showroom")

    def __str__(self):
        return f"History{self.id}"
