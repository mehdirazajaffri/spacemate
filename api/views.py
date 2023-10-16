from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from api.serializers import (
    PropertySerializer,
    AmenitySerializer,
    RoomSerializer,
    BookingSerializer,
    ReviewSerializer,
    UserSerializer,
)
from app.models import Property, Amenity, Room, Booking, Review
from user.models import UserProfile


class BaseViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend, SearchFilter)


class PropertyViewSet(BaseViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_fields = ("city",)
    search_fields = (
        "title",
        "description",
        "address",
        "city",
        "area",
        "location",
    )


class AmenityViewSet(BaseViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    search_fields = ("name",)


class RoomViewSet(BaseViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    search_fields = (
        "title",
        "description",
        "room_type",
    )
    filter_fields = (
        "room_type",
        "is_available",
        "max_beds",
        "vacant_beds",
        "available_from",
    )


class BookingViewSet(BaseViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    search_fields = (
        "guest__first_name",
        "guest__last_name",
        "room__title",
        "room__description",
    )
    filter_fields = (
        "guest",
        "room",
        "check_in",
        "check_out",
    )


class ReviewViewSet(BaseViewSet):  # all done?
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    search_fields = (
        "guest__first_name",
        "guest__last_name",
        "room__title",
        "room__description",
    )
    filter_fields = (
        "guest",
        "room",
        "rating",
    )


class UserViewSet(BaseViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    search_fields = (
        "user__first_name",
        "user__last_name",
        "email",
    )
    filter_fields = (
        "user__first_name",
        "user__last_name",
        "email",
    )
