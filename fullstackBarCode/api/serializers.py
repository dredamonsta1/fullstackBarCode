from rest_framework import serializers
from .model import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'product', 'can_add_photo', 'vote_as_damaged', 'created_at')