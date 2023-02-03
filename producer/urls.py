from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers

from producer.views import ShowRoomViewSet

router = routers.SimpleRouter()
router.register(r'producers', ShowRoomViewSet)

urlpatterns = router.urls
