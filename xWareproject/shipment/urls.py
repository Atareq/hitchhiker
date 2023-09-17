from django.urls import path
from .viewset import ShipmentViewSet ,ShipmentItemViewSet
from .views import create_shipment_item ,myshipment_view_set

urlpatterns =[

    path('',ShipmentViewSet.as_view(
        {'get':'list',
         'post':'partial_update'
        })),
    path('add/', create_shipment_item),
    path('my/', myshipment_view_set)

]

