from rest_framework import serializers

from car.models import AvailableCar


class CarSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="available_car.name", read_only=True)

    class Meta:
        model = AvailableCar
        fields = ["available_car", "count", "price", "name"]
        extra_kwargs = {"available_car": {"write_only": True}}
