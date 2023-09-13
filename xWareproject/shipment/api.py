from django.shortcuts import render
from rest_framework import viewsets 
from .models import Shipment ,ShipmentItem
from .serializers import ShipmentSerializer ,ItemShipmentSerializer
from django_filters.rest_framework import DjangoFilterBackend 
from django_filters import rest_framework as filters
from .filters import ShipmentFilters , ShipmentItemFilters


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShipmentFilters 


class ShipmentItemViewSet (viewsets.ModelViewSet):
    queryset=ShipmentItem.objects.all()
    serializer_class = ItemShipmentSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=ShipmentItemFilters