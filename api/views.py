from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView

# Create your views here.
from .models import Room
from .serializers import RoomSerializer

class RoomView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
