from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers

from showroom.views import ShowRoomViewSet, showrooms_list, showroom_detail

router = routers.SimpleRouter()
router.register(r"showrooms", ShowRoomViewSet)

urlpatterns = [
                  # API маршрут для get_showrooms
                  path(
                      "a_showrooms/",
                      ShowRoomViewSet.as_view({"get": "get_showrooms"}),
                      name="show_showrooms",
                  ),

                  # HTML маршруты
                  path("showrooms/", showrooms_list, name="showrooms_list"),
                  path("showrooms/<int:pk>/", showroom_detail, name="showroom_detail"),
              ] + router.urls