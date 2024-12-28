from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from producer.models import Producer

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

    @action(detail=False, methods=["GET"], permission_classes=[AllowAny])
    def html_list(self, request):
        """Эндпоинт для рендеринга списка продюсеров."""
        producers = self.get_queryset()
        return render(request, 'producer/producers_list.html', {'producers': producers})

    @action(detail=True, methods=["GET"], permission_classes=[AllowAny])
    def html_detail(self, request, pk=None):
        """Эндпоинт для рендеринга деталей продюсера."""
        producer = get_object_or_404(Producer, pk=pk)
        return render(request, 'producer/producer_detail.html', {'producer': producer})