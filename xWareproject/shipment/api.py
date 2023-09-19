from django.db.models import Q
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view, action
from .serializers import ShipmentSerializer, ShipmentItemSerializer
from info_from_token import get_user_pk_from_token
from .models import Shipment, ShipmentItem, Trip
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ShipmentFilters , ShipmentItemFilters



class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShipmentFilters 

    # http_method_names = ['GET']

    def list(self,request):

        query = Shipment.objects.filter(trip_object__isnull=True)
        shepment_serialized = ShipmentSerializer(instance=query, many=True) 
        # shepment_serialized.is_valid()
        return Response(shepment_serialized.data, status=status.HTTP_200_OK)    


    def retrieve(self, request, *args, **kwargs):
        
        query = Shipment.objects.filter(id=kwargs['pk']).first()
        shepment_serialized = ShipmentSerializer(instance=query) 
        return Response(shepment_serialized.data, status=status.HTTP_200_OK)    
 
    
    def create(self, request):
        print("taaareq"*100)
        shipment_and_item = request.data  
        # Get the user's PK from the token
        user_pk = get_user_pk_from_token(request)

        if user_pk is None:
            return Response({"error": "Invalid or missing token"}, status=status.HTTP_401_UNAUTHORIZED)

        shipment_and_item['user_s'] = user_pk

        # Create instances of Shipment and ShipmentItem serializers
        shipment_serializer = ShipmentSerializer(data=shipment_and_item)
        item_serializer = ShipmentItemSerializer(data=shipment_and_item)
        shipment_and_item['shipment_weight'] = shipment_and_item.get('item_weight', None)

        shipment_serializer.is_valid(raise_exception=True)
        ship_instance = shipment_serializer.save()
        
        shipment_and_item['shipment_id'] = ship_instance.id
        item_serializer.is_valid(raise_exception=True)
        item_instance = item_serializer.save()
        ship_instance.shipment_weight += item_instance.item_weight
        ship_instance.save()
        
        # Return a success response
        return Response(item_serializer.data, status=status.HTTP_201_CREATED)

    def link_shipment_trip(self, request):
        trip_pk = request.data.get('trip_pk')
        shipment_pk = request.data.get('shipment_pk')
        
        # Check if the Shipment and Trip objects exist
        if not Shipment.objects.filter(id=shipment_pk).exists() or not Trip.objects.filter(id=trip_pk).exists():
            return Response({"error": "Shipment or Trip does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve the objects
        shipment_object = Shipment.objects.get(id=shipment_pk)
        trip_object = Trip.objects.get(id=trip_pk)
        
        # Update the shipment's trip_object
        shipment_object.trip_object = trip_object
        shipment_object.save()
        
        return Response(status=status.HTTP_200_OK)

    def myshipment(self, request):
        user_pk = get_user_pk_from_token(request=request)
        my_shipment_objects = Shipment.objects.filter(user_s=user_pk)
        serialized_shipment = ShipmentSerializer(my_shipment_objects, many=True)
        myshipments_data = serialized_shipment.data
        return Response(myshipments_data, status=status.HTTP_200_OK)



    # def create(self, request):
    #     item_data = request.data.get('item', {})  # Assuming 'item' is the data for ShipmentItem
    #     shipment_data = request.data.get('shipment', {})  # Assuming 'shipment' is the data for Shipment

    #     # Get the user's PK from the token
    #     user_pk = get_user_pk_from_token(request)

    #     if user_pk is None:
    #         return Response({"error": "Invalid or missing token"}, status=status.HTTP_401_UNAUTHORIZED)

    #     shipment_data['user_s'] = user_pk

    #     # Create instances of Shipment and ShipmentItem serializers
    #     shipment_serializer = ShipmentSerializer(data=shipment_data)
    #     item_serializer = ShipmentItemSerializer(data=item_data)
    #     shipment_data['shipment_weight'] = item_data.get('item_weight', None)

    #     shipment_serializer.is_valid(raise_exception=True)
    #     ship_instance = shipment_serializer.save()
        
    #     item_data['shipment_id'] = ship_instance.id
    #     item_serializer.is_valid(raise_exception=True)
    #     item_instance = item_serializer.save()
    #     ship_instance.shipment_weight += item_instance.item_weight
    #     ship_instance.save()
        
    #     # Return a success response
    #     return Response(item_data, status=status.HTTP_201_CREATED)
