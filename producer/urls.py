from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers

from producer.views import ProducerViewSet

router = routers.SimpleRouter()
router.register(r'producers', ProducerViewSet)

urlpatterns = router.urls
