from django.urls import path
from conversations import views as conversation_views

app_name = "conversations"

urlpatterns = [path("", conversation_views.all_conversations, name="conversations")]

