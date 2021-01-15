from django.shortcuts import render
from conversations.models import Conversation


def all_conversations(request):

    all_conversations = Conversation.objects.all()[:5]

    context = {"conversations": all_conversations}

    return render(request, "conversations/all_conversations.html", context)

