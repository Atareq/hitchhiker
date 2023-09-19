from rest_framework import serializers
from .models import Shipment,Trip ,ShipmentItem



class ShipmentItemSerializer(serializers.ModelSerializer):
    # user_shipment = ShipmentSerializer(many=True)

    class Meta :
        model = ShipmentItem
        fields = '__all__'

class RetriveShipmentSerializer(serializers.ModelSerializer):
    items = ShipmentItemSerializer(source="shipmentitem_set", many=True)

    class Meta:
        model = Shipment
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipment
        fields = '__all__'

    # def Create(self , validated_data):
    #     user_shipment = validated_data.pop('user shipment')
    #     item_instance = ShipmentItem.objects.create(**validated_data)

    #     for ship in user_shipment:
    #         Shipment.objects.create(user = item_instance ,**ship)
    #     return item_instance
    

