import uuid

from django.db import models

from app.constant import CITIES
from core.models import BaseModel
from user.models import UserProfile


class Amenity(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"


class Property(BaseModel):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(choices=CITIES, max_length=50)
    area = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    amenities = models.ManyToManyField(Amenity, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"


class Room(BaseModel):
    property = models.ForeignKey("Property", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    room_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    max_beds = models.PositiveIntegerField()
    vacant_beds = models.PositiveIntegerField()
    amenities = models.ManyToManyField("Amenity", blank=True)
    available_from = models.DateField()
    restriction = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"


class Image(BaseModel):
    property = models.ForeignKey(
        "Property", on_delete=models.CASCADE, blank=True, null=True
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="property_images")
    is_featured = models.BooleanField(default=False)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Booking(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    guest = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    is_confirmed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    is_checked_in = models.BooleanField(default=False)
    is_checked_out = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    payment_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.room.title if self.room else ""

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"


class Review(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    is_moderated = models.BooleanField(default=False)
