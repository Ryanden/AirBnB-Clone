from django.urls import path
from rooms import views as room_views

app_name = "rooms"

urlpatterns = [path("", room_views.RoomView.as_view(), name="rooms")]
