from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers

from car.views import ModelViewSet

router = routers.SimpleRouter()
router.register(r'cars', ModelViewSet)

urlpatterns = router.urls
