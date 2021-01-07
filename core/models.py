from django.db import models


class TimeStampModel(models.Model):

    """Time Stapmped Definition"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

