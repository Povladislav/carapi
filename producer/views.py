from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from producer.models import Producer
from producer.serializers import ProducerSerializer


class ProducerFilter(FilterSet):
    class Meta:
        model = Producer
        fields = {
            "title": ["icontains"],
            "year_of_establishment": ["icontains"],
        }


class ProducerViewSet(ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["title"]
    ordering_fields = ["title", "year_of_establishment"]
    filterset_class = ProducerFilter
