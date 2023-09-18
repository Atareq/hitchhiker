

from rest_framework.response import Response
from rest_framework import status
from .serializers import ShipmentSerializer, ShipmentItemSerializer
from rest_framework.decorators import api_view
from info_from_token import get_user_pk_from_token
from .models import Shipment 
from django.shortcuts import render
from rest_framework import viewsets 
from .models import Shipment ,ShipmentItem , Trip
from .serializers import ShipmentSerializer ,ShipmentItemSerializer ,ShipmentUpdateSerializer
from django_filters.rest_framework import DjangoFilterBackend 
from .filters import ShipmentFilters , ShipmentItemFilters
from info_from_token import get_user_pk_from_token
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShipmentFilters 

    
    def link_trip_to_shipment(self, request):    
        trip_pk= request.data.get('trip_pk')
        shipment_pk = request.data.get('shimpment_pk')
        shipment_object = Shipment.objects.get(id=shipment_pk)
        trip_object = Trip.objects.get(id=trip_pk)
        shipment_object.trip_object = trip_object
        shipment_object.save()
        return Response (status=status.HTTP_200_OK)
 



class ShipmentItemViewSet (viewsets.ModelViewSet):
    queryset=ShipmentItem.objects.filter()
    serializer_class = ShipmentItemSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=ShipmentItemFilters


@api_view(['POST'])
def create_shipment_item(request):
    item_data = request.data.get('item', {})  # Assuming 'item' is the data for ShipmentItem
    shipment_data = request.data.get('shipment', {})  # Assuming 'shipment' is the data for Shipment

    # Get the user's PK from the token
    user_pk = get_user_pk_from_token(request)

    if user_pk is None:
        return Response({"error": "Invalid or missing token"}, status=status.HTTP_401_UNAUTHORIZED)

    shipment_data['user_s'] = user_pk

    # Create instances of Shipment and ShipmentItem serializers
    shipment_serializer = ShipmentSerializer(data=shipment_data)
    shipment_serializer.is_valid(raise_exception=True)
    ship_instance = shipment_serializer.save()

    item_data['shipment_id'] = ship_instance.id
    item_serializer = ShipmentItemSerializer(data=item_data)
    item_serializer.is_valid(raise_exception=True)
    item_serializer.save()

    # Return a success response
    return Response(item_data, status=status.HTTP_201_CREATED)




@api_view(['GET'])
def  myshipment_view_set(request):
    user_pk = get_user_pk_from_token(request=request)
    my_shipment_objects = Shipment.objects.filter(user_s=user_pk)
    serialized_shipment = ShipmentSerializer(my_shipment_objects, many=True)
    myshipments_data = serialized_shipment.data
    return Response(myshipments_data, status=status.HTTP_200_OK)