from django.urls import path
from .viewset import ShipmentViewSet ,ShipmentItemViewSet
from .views import create_shipment_item ,myshipment_view_set

# urlpatterns =[

#     path('',ShipmentViewSet.as_view(
#         {'get':'list',
#          'post':'partial_update'
#         })),
#     path('add/', create_shipment_item),
#     path('my/', myshipment_view_set)

# ]
from django.urls import path , include
from .viewset import ShipmentViewSet 

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'shipment', ShipmentViewSet)  

urlpatterns = [
    path('api/', include(router.urls)),
    path('add/', create_shipment_item),
    path('my/', myshipment_view_set)
]

