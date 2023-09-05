from django.contrib import admin
from django.urls import path , include
from trip.api import TripViewSet 
from shipment.api import ShipmentItemViewSet,ShipmentViewSet
# from shipment.api import ShipmentViewSet

urlpatterns = [

    path('admin/', admin.site.urls),
    path('trip/',include('trip.urls')),
    path('shipment/',include('shipment.urls')),
    
]   
