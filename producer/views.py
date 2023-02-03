from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet

from producer.models import Producer
from producer.serializers import ProducerSerializer


class ProducerViewSet(ModelViewSet):
    queryset = Producer.objects.all()
    permission_classes = [AllowAny]  # FOR TEST ITS [ALLOWANY] but in PRODUCTION it will be [IsAdminUser]
    serializer_class = ProducerSerializer
