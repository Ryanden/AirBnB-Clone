from django.urls import path
from conversations import views as message_views

app_name = "message"

urlpatterns = [path("", message_views.MessageView.as_view(), name="message")]

