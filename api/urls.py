from django.urls import path

from .views import RoomView

urlpatterns = [
    path('room', RoomView.as_view()),
    # path('<int:pk>', RoomDetailView.as_view())
]