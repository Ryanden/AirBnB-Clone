from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAmdin(UserAdmin):

    list_display = (
        "username",
        "gender",
        "language",
        "currency",
    )
    list_filter = (
        "superhost",
        "gender",
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
