from django.urls import path
from . import trip_api
from .trip_api import TripViewSet
from .my_trip_api import MyTripViewSet

urlpatterns =[
     path('',TripViewSet.as_view(
        {
        'get':'list',
         'post':'create'
         }
         )),
     path ('my',MyTripViewSet.as_view({
         
         'post'':patch'
     })),
    
    path('<int:pk>/',TripViewSet.as_view(
        {
         'get':'retrieve' ,
         'post':'create',
         'patch':'partial_update',
         'put' : 'update',
         'delete' : 'destroy',
        })),

]