from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from showroom.models import ShowRoom
from showroom.serializers import ShowRoomSerializer


class SRFilter(FilterSet):
    class Meta:
        model = ShowRoom
        fields = {
            'balance': ['lt', 'gt'],
            'title': ['icontains']
        }


class ShowRoomViewSet(ModelViewSet):
    queryset = ShowRoom.objects.all()
    serializer_class = ShowRoomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['balance', 'title']
    ordering_fields = ['balance']
    filterset_class = SRFilter
