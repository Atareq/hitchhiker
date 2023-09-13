from django.contrib import admin
from django.urls import path , include
from trip.trip_api import TripViewSet 
from shipment.api import ShipmentItemViewSet,ShipmentViewSet
# from Users.views import UserDetailAPI , RegisterUserAPIView

# from shipment.api import ShipmentViewSet
urlpatterns = [

    # path("get-details",UserDetailAPI.as_view()),
    # path('register',RegisterUserAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('user/',include('User_auth.urls')),

    path('trip/',include('trip.urls')),
    path('shipment/',include('shipment.urls')),
    
]   
