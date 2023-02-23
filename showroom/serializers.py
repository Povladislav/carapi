from rest_framework import serializers

from showroom.models import ShowRoom


class ShowRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowRoom
        fields = "__all__"
