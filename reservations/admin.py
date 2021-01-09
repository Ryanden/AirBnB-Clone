from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ResercationAdmin(admin.ModelAdmin):

    """ Resercation Admin Definition """

    pass
