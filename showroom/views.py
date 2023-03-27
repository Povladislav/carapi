from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from showroom.models import ShowRoom
from showroom.serializers import ShowRoomSerializer, ShowRoomSerializerForAdmin


class SRFilter(FilterSet):
    class Meta:
        model = ShowRoom
        fields = {"balance": ["lt", "gt"], "title": ["icontains"]}


class ShowRoomViewSet(ModelViewSet):
    queryset = ShowRoom.objects.all()
    serializer_class = ShowRoomSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["balance", "title"]
    ordering_fields = ["balance"]
    filterset_class = SRFilter

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['GET'], permission_classes=[IsAdminUser])
    def get_showrooms(self, request):
        showrooms = ShowRoom.objects.all()
        serializer = ShowRoomSerializerForAdmin(showrooms, many=True)
        return Response(serializer.data)
