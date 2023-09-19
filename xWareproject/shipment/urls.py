from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ShipmentViewSet

router = DefaultRouter()
router.register(r'shipment', ShipmentViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Add a custom URL route for the link_shipment_trip action
    path('link_shipment_trip/', ShipmentViewSet.as_view({'post': 'link_shipment_trip'}), name='link_shipment_trip'),
    path('myshipment/', ShipmentViewSet.as_view({'get': 'myshipment'}), name='myshipment'),
]
