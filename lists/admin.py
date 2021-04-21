from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Lists)
class ListAdmin(admin.ModelAdmin):
    """List Model Admin"""

    list_display = ("name", "user", "count_rooms")

    search_fields = ("name",)

    filter_horizontal = ("rooms",)