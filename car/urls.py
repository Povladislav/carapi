from rest_framework import routers

from car.views import CarViewSet

router = routers.SimpleRouter()
router.register(r'cars', CarViewSet)

urlpatterns = router.urls
