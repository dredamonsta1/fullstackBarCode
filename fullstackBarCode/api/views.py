from django.shortcuts import render
from rest_framework import generics
from .serializers import CreateBarcodeSerializer, RoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class createRoomView(APIView):
    serializer_class = CreateBarcodeSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            barcode_to_add = serializer.data.barcode_to_add
            barcode_image = serializer.data.barcode_image