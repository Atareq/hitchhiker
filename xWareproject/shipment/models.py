from django.db import models
from trip.models import Trip

cities_of_travel =[
    ('usa','United Status America'),
    ('ca','canada'),
    ('kwt','kewit'),
    ('egy','egypt'),
    ('ksa','saudi')
    ]

class Shipment(models.Model):
    
    from_location = models.CharField(choices = cities_of_travel,max_length=20)
    to_location = models.CharField(choices = cities_of_travel,max_length=20)
    name_shipment = models.CharField(max_length=20)
    before_date = models.DateField(auto_now_add=True)
    trip_object =  models.ForeignKey(Trip ,on_delete=models.CASCADE)

class ShipmentItem(models.Model):

    shipment_id = models.ForeignKey(Shipment,on_delete=models.CASCADE)
    item_link = models.URLField()
    item_name = models.CharField(max_length=100)
    item_quantity = models.IntegerField()
    item_weight = models.FloatField()
    single_item_price = models.DecimalField(max_digits=8, decimal_places=2)
    