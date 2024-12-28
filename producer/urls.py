from django.urls import path, include
from rest_framework.routers import SimpleRouter
from producer.views import ProducerViewSet

router = SimpleRouter()
router.register(r"producers", ProducerViewSet)

urlpatterns = [
    # API маршруты
    path('', include(router.urls)),

    # HTML маршруты
    path('producers/html/', ProducerViewSet.as_view({'get': 'html_list'}), name='producers_list'),
    path('producers/html/<int:pk>/', ProducerViewSet.as_view({'get': 'html_detail'}), name='producer_detail'),
]