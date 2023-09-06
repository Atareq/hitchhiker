from django.urls import path
from . import api
from .api import TripViewSet



urlpatterns =[

     path('',TripViewSet.as_view(
        {
        'get':'list',
         'post':'create'
         }
         )),
    
    path('<int:pk>/',TripViewSet.as_view(
        {
         'get':'retrieve' ,
         'post':'create',
         'patch':'partial_update',
         'put' : 'update',
         'delete' : 'destroy',
        })),

]