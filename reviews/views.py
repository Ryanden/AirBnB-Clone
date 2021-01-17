from django.views.generic import ListView
from . import models


class ReviewView(ListView):
    """ Review Definition """

    model = models.Review
    paginate_by = 10
    paginate_orphans = 5
    ordering = "pk"

