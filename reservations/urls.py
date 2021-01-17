from django.urls import path
from reservations import views as reservation_views

app_name = "reservation"

urlpatterns = [
    path("", reservation_views.ReservationView.as_view(), name="reservation")
]

