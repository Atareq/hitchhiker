from django.shortcuts import render
from rest_framework import viewsets
from .models import Shipment ,ShipmentItem
from .serializers import ShipmentSerializer ,ItemShipmentSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    
class ShipmentItemViewSet (viewsets.ModelViewSet):
    queryset=ShipmentItem.objects.all()
    serializer_class = ItemShipmentSerializer