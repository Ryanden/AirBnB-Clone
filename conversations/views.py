from django.views.generic import ListView
from . import models


class MessageView(ListView):
    """ MessageView Definition """

    model = models.Message
    paginate_by = 10
    paginate_orphans = 5
    ordering = "pk"

