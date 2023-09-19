from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import  TripViewSet


router = DefaultRouter()
router.register(r'trip', TripViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('mytrip/', TripViewSet.as_view({'get':'mytrip'}), name='my-trips'),
]
