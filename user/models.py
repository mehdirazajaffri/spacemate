from django.contrib.auth.models import User
from django.db import models

from app.constant import CITIES
from core.models import BaseModel


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(choices=CITIES, max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures", blank=True, null=True
    )
    bio = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_property_owner = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.email}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
