# Generated by Django 4.2.6 on 2023-10-16 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "city",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("dubai", "Dubai"),
                            ("abu-dhabi", "Abu Dhabi"),
                            ("sharjah", "Sharjah"),
                            ("ajman", "Ajman"),
                            ("ras-al-khaimah", "Ras Al Khaimah"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_pictures"
                    ),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                ("is_verified", models.BooleanField(default=False)),
                ("is_email_verified", models.BooleanField(default=False)),
                ("is_property_owner", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User Profile",
                "verbose_name_plural": "User Profiles",
            },
        ),
    ]
