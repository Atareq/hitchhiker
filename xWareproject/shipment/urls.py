from django.urls import path
from .viewset import ShipmentViewSet ,ShipmentItemViewSet
from .views import create_shipment_item

urlpatterns =[

    path('',ShipmentViewSet.as_view(
        {'get':'list',
        })),
    path('add/', create_shipment_item),
    
    path('<int:pk>/',ShipmentItemViewSet.as_view(
        {
         'get':'retrieve' ,
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

