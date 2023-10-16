from django.contrib import admin

from app.models import Amenity, Property, Room, Booking, Image


class BaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    save_on_top = True


@admin.register(Amenity)
class AmenityAdmin(BaseAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(Property)
class PropertyAdmin(BaseAdmin):
    list_display = (
        'title', 'owner', 'city', 'price', 'is_available', 'is_featured', 'is_verified', 'created_at', 'updated_at')
    list_filter = ('is_available', 'is_featured', 'is_verified', 'city')
    search_fields = ('title', 'description', 'address', 'city', 'area', 'location',)
    list_editable = ('is_available', 'is_featured', 'is_verified',)
    autocomplete_fields = ('owner',)


@admin.register(Room)
class RoomAdmin(BaseAdmin):
    list_display = (
        'title', 'property', 'room_type', 'price', 'is_available', 'max_beds', 'vacant_beds', 'available_from',
        'created_at', 'updated_at')
    list_filter = ('is_available', 'room_type', 'amenities',)
    search_fields = ('title', 'description', 'room_type',)
    autocomplete_fields = ('property',)


@admin.register(Booking)
class BookingAdmin(BaseAdmin):
    list_display = (
        'id', 'room', 'guest', 'check_in', 'check_out', 'is_confirmed', 'total_amount', 'created_at', 'updated_at')
    list_filter = ('check_in', 'check_out',)
    search_fields = ('room__title', 'guest__user__username', 'check_in', 'check_out',)
    autocomplete_fields = ('guest', 'room',)


@admin.register(Image)
class ImageAdmin(BaseAdmin):
    list_display = ('name', 'property', 'room', 'is_featured', 'created_at', 'updated_at')
    list_filter = ('is_featured',)
    search_fields = ('name', 'property', 'room',)
