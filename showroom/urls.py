from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers

from showroom.views import ShowRoomViewSet

router = routers.SimpleRouter()
router.register(r'showrooms', ShowRoomViewSet)

urlpatterns = router.urls
