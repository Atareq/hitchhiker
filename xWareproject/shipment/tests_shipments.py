from django.test import TestCase
from .models import Shipment, ShipmentItem
from User_auth.models import CustomUser
from datetime import date

class ShipmentModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="testuser")
        self.shipment = Shipment.objects.create(
            user_s=self.user,
            from_location="usa",
            to_location="canada",
            name_shipment="Test Shipment",
            before_date=date.today(),
        )

    def test_shipment_creation(self):
        self.assertEqual(self.shipment.user_s, self.user)
        self.assertEqual(self.shipment.from_location, "usa")
        self.assertEqual(self.shipment.to_location, "canada")
        self.assertEqual(self.shipment.name_shipment, "Test Shipment")

class ShipmentItemModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="testuser")
        self.shipment = Shipment.objects.create(
            user_s=self.user,
            from_location="usa",
            to_location="canada",
            name_shipment="Test Shipment",
            before_date=date.today(),
        )
        self.shipment_item = ShipmentItem.objects.create(
            shipment_id=self.shipment,
            item_link="https://example.com/item",
            item_name="Test Item",
            item_weight=2.5,
            single_item_price=19.99,
            rate=4,
        )

    def test_shipment_item_creation(self):
        self.assertEqual(self.shipment_item.shipment_id, self.shipment)
        self.assertEqual(self.shipment_item.item_link, "https://example.com/item")
        self.assertEqual(self.shipment_item.item_name, "Test Item")
        self.assertEqual(self.shipment_item.item_weight, 2.5)
        self.assertEqual(self.shipment_item.single_item_price, 19.99)
        self.assertEqual(self.shipment_item.rate, 4)
