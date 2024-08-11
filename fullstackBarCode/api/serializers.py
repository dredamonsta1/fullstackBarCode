from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'product', 
                  'can_add_photo', 'vote_as_damaged', 
                  'created_at')
        
class CreateBarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('barcode_to_add', 'barcode_image')