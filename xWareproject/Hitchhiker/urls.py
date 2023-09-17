from django.contrib import admin
from django.urls import path , include
from shipment.viewset import ShipmentItemViewSet,ShipmentViewSet
# from Users.views import UserDetailAPI , RegisterUserAPIView

# from shipment.api import ShipmentViewSet
urlpatterns = [

    path('admin/', admin.site.urls),
    path('user/',include('User_auth.urls')),

    path('trip/',include('trip.urls')),

    path('shipment/',include('shipment.urls')),
    
]   
