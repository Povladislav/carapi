from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers

from showroom.views import ShowRoomViewSet

router = routers.SimpleRouter()
router.register(r"showrooms", ShowRoomViewSet)

urlpatterns = [
    path(
        "a_showrooms/",
        ShowRoomViewSet.as_view({"get": "get_showrooms"}),
        name="show_showrooms",
    )
] + router.urls
