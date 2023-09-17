from django.urls import path
from .trip_api import TripViewSet
# from .views import MyTripViewSet


urlpatterns =[
     path('',TripViewSet.as_view(
 {
        'get':'list',
        'post':'create',
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
    #  path('my/',MyTripViewSet)

]

##shippment id w di hadfha any a3rf a3ml share ll 7aga ally 3ayzha