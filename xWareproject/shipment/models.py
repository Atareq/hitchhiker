from django.db import models
from trip.models import Trip

cities_of_travel =[('usa','United Status America'),
    ('ca','canada'),('kwt','kewit'),('egy','egypt'),
    ('ksa','saudi')]

class Shipment(models.Model):
    item_link = models.URLField()
    item_name = models.CharField(max_length=100)
    item_quantity = models.IntegerField()
    single_item_price = models.DecimalField(max_digits=8, decimal_places=2)
    from_location = models.CharField(choices = cities_of_travel)
    to_location = models.CharField(choices = cities_of_travel)
    weight_ship = models.FloatField()
    before_date = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=500)
    user_shipment = models.ForeignKey(Trip,on_delete=models.CASCADE)

class item(models.Model):
    shipment_item = models.ForeignKey(Shipment,on_delete=models.CASCADE)
