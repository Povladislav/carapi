from rest_framework import serializers

from car.serializers import CarSerializer
from producer.models import Producer


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"
