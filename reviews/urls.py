from django.urls import path
from reviews import views as review_views

app_name = "reviews"

urlpatterns = [path("", reviews.ReviewView.as_view(), name="reviews")]

