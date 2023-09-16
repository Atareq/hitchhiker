from django.db import models
from trip.models import Trip
from User_auth.models import CustomUser
from django.core.validators import MaxValueValidator ,MinValueValidator

cities_of_travel =[
    ('usa','United Status America'),
    ('ca','canada'),
    ('kwt','kewit'),
    ('egy','egypt'),
    ('ksa','saudi')

    ]

class Shipment(models.Model):

    user_s=models.ForeignKey(CustomUser, null=False,on_delete=models.CASCADE )    
    from_location = models.CharField(choices = cities_of_travel,max_length=20)
    to_location = models.CharField(choices = cities_of_travel,max_length=20)
    name_shipment = models.CharField(max_length=20)
    before_date = models.DateField()
    # trip_object =  models.ForeignKey(Trip ,null=True,default=None,on_delete=models.CASCADE)

class ShipmentItem(models.Model):
    shipment_id = models.ForeignKey(Shipment,on_delete=models.CASCADE)
    item_link = models.URLField()
    item_name = models.CharField(max_length=100)
    item_weight = models.FloatField()
    single_item_price = models.DecimalField(max_digits=8, decimal_places=2)
    rate = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    # item_quantity = models.IntegerField()
    #item_image = models.ImageField()


 
    #a3mlo bilpostgres