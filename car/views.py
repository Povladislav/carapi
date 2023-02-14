from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from car.models import AvailableCar
from car.serializers import CarSerializer


class CarFilter(FilterSet):
    class Meta:
        model = AvailableCar
        fields = {
            'price': ['lt', 'gt'],
        }


class CarViewSet(ModelViewSet):
    queryset = AvailableCar.objects.all()
    permission_classes = [AllowAny]  # FOR TEST ITS [ALLOWANY] but in PRODUCTION it will be [IsAdminUser]
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['price']
    ordering_fields = ['price']
    filterset_class = CarFilter
