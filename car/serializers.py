from rest_framework import serializers

from car.models import AvailableCar


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = AvailableCar
        fields = ["available_car", "count", "price"]
