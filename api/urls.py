from django.urls import path

from .views import RoomDetailView, RoomListView

urlpatterns = [
    path('', RoomListView.as_view()),
    path('<int:pk>', RoomDetailView.as_view())
]