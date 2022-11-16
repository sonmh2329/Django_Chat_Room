from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

# Create your views here.
from .models import Room
from .serializers import RoomSerializer

class RoomListView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class RoomDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
