from django.urls import path
from . import api
from .api import ShipmentViewSet ,ShipmentItemViewSet


urlpatterns =[

    path('',ShipmentViewSet.as_view(
        {'get':'list',
         'post':'create'})),
    
    path('<int:pk>/',ShipmentViewSet.as_view(
        {
         'get':'retrieve' ,
         'post':'create',
         'patch':'partial_update',
         'put' : 'update',
         'delete' : 'destroy',
        })),

    path ('item/',ShipmentItemViewSet.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path('item/<int:pk>/',ShipmentItemViewSet.as_view(
        {
         'get':'retrieve' ,
         'post':'create',
         'patch':'partial_update',
         'put' : 'update',
         'delete' : 'destroy',
        })),

]

