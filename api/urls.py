from django.urls import path, include
from rest_framework import routers

from api.views import (
    PropertyViewSet,
    RoomViewSet,
    BookingViewSet,
    ReviewViewSet,
    UserViewSet,
)

router = routers.DefaultRouter()
router.register("property", PropertyViewSet)
router.register("room", RoomViewSet)
router.register("booking", BookingViewSet)
router.register("review", ReviewViewSet)
router.register("user", UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
