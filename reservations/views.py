from django.views.generic import ListView
from . import models


class ReservationView(ListView):
    """ ReservationView Definition """

    model = models.Reservation
    paginate_by = 10
    paginate_orphans = 5
    ordering = "pk"

