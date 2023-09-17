from django.urls import path
from .trip_api import TripViewSet
from .views import add_trip
from .trip_api import mytrip_view_set

urlpatterns =[
     path('',TripViewSet.as_view(
 {
        'get':'list',
         }
         )),
    #  path ('my',MyTripViewSet.as_view({
    #      'post'':patch'
    #  })),
    
    path('<int:pk>/',TripViewSet.as_view(
        {
         'get':'retrieve' ,
         'patch':'partial_update',
        }))
        ,
     path('add/',add_trip),

     path('my/',mytrip_view_set),

]

##shippment id w di hadfha any a3rf a3ml share ll 7aga ally 3ayzha