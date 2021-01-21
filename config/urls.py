from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("conversations/", include("conversations.urls", namespace="conversations")),
    path("users/", include("users.urls", namespace="users")),
    # path("lists/", include("lists.urls", namespace="lists")),
    # path("reservations/", include("reservations.urls", namespace="reservations")),
    # path("reviews/", include("reviews.urls", namespace="reviews")),
    path("rooms/", include("rooms.urls", namespace="rooms")),
    path("admin/", admin.site.urls),
]
