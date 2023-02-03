from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from producer.models import Producer
from producer.serializers import ProducerSerializer


class ShowRoomViewSet(ModelViewSet):
    queryset = Producer.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ProducerSerializer
