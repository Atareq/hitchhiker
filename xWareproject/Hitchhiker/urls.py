from django.contrib import admin
from django.urls import path ,include
urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include('User_auth.urls')),

    path('',include('trip.urls')),

    path('',include('shipment.urls')),
    
]   
