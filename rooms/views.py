from django.shortcuts import render
from rooms.models import Room


def all_rooms(request):

    all_rooms = Room.objects.all()[:5]

    context = {"rooms": all_rooms}

    return render(request, "rooms/rooms.html", context)

