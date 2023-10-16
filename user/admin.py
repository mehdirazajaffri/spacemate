from django.contrib import admin

from user.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "phone",
        "email",
        "address",
        "city",
        "created_at",
        "updated_at",
    )
    list_filter = ("city",)
    search_fields = ("user", "phone", "address", "city", "user__username")
    readonly_fields = (
        "created_at",
        "updated_at",
        "deleted_at",
    )
