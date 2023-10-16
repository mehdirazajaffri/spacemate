from rest_framework import serializers

from app.models import Property, Amenity, Room, Booking, Review
from user.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Property
        fields = "__all__"


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class RoomDetailSerializer(RoomSerializer):
    property = PropertySerializer(read_only=True)
    amenities = AmenitySerializer(read_only=True, many=True)


class BookingSerializer(serializers.ModelSerializer):
    guest = UserSerializer(read_only=True)
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    guest = UserSerializer(read_only=True)
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"
