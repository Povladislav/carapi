from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import filters
from car.models import Car
from car.serializers import CarSerializer


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'price': ['lt', 'gt'],
            'name': ['icontains']
        }


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['price']
    ordering_fields = ['price']
    filterset_class = CarFilter
