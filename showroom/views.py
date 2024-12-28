from django.shortcuts import render
from rest_framework.decorators import action

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
        if self.action == "list":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=["GET"], url_path='html-list', permission_classes=[AllowAny])
    def html_list(self, request):
        """Эндпоинт для отображения HTML-страницы со списком шоурумов."""
        showrooms = self.get_queryset()
        return render(request, 'showroom/showrooms_list.html', {'showrooms': showrooms})

    @action(detail=True, methods=["GET"], url_path='html-detail', permission_classes=[AllowAny])
    def html_detail(self, request, pk=None):
        """Эндпоинт для отображения HTML-страницы с деталями шоурума."""
        showroom = get_object_or_404(ShowRoom, pk=pk)
        return render(request, 'showroom/showroom_detail.html', {'showroom': showroom})