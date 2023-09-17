from django.shortcuts import render
from rest_framework import viewsets 
from .models import Shipment ,ShipmentItem
from .serializers import ShipmentSerializer ,ShipmentItemSerializer
from django_filters.rest_framework import DjangoFilterBackend 
from django_filters import rest_framework as filters
from .filters import ShipmentFilters , ShipmentItemFilters
from info_from_token import get_user_pk_from_token

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShipmentFilters 
    # def retrieve(request):
    #     user_pk=get_user_pk_from_token(request=request)




class ShipmentItemViewSet (viewsets.ModelViewSet):
    queryset=ShipmentItem.objects.filter()
    serializer_class = ShipmentItemSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=ShipmentItemFilters