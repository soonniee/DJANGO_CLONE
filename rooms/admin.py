from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    fielsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "Spaces",
            {
                "fields": (
                    "amenities",
                    "facilties",
                    "house_rules",
                )
            },
        ),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("guests", "beds", "bedrooms", "baths"),
            },
        ),
        (
            "Last Details",
            {"fields": ("host")},
        ),
    )
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_photos",
    )
    list_filter = (
        "instant_book",
        "room_type",
        "amenities",
        "facilties",
        "house_rules",
        "country",
        "city",
    )
    search_fields = ("=city", "^host__username")
    filter_horizontal = (
        "amenities",
        "facilties",
        "house_rules",
    )

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass