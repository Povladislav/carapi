from rest_framework import serializers

from car.models import Car, ModelName


class CarSerializer(serializers.ModelSerializer):
    model = serializers.CharField(source='model.title')
    color = serializers.CharField(source='color.title')

    class Meta:
        model = Car
        fields = ['name', 'model', 'color', 'power', 'price']
