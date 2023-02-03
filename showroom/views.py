from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from showroom.models import ShowRoom
from showroom.serializers import ShowRoomSerializer


class ShowRoomViewSet(ModelViewSet):
    queryset = ShowRoom.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ShowRoomSerializer
