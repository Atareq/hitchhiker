from rest_framework.response import Response
from rest_framework import status
from .serializers import ShipmentSerializer, ShipmentItemSerializer
from rest_framework.decorators import api_view
from info_from_token import get_user_pk_from_token


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
    return Response(item_data, shipment_data, status=status.HTTP_201_CREATED)


