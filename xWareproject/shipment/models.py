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

    user_s  = models.ForeignKey(CustomUser, null=False,on_delete=models.CASCADE )    
    from_location = models.CharField(choices = cities_of_travel,max_length=20,blank=False)
    to_location = models.CharField(choices = cities_of_travel,max_length=20,blank=False)
    name_shipment = models.CharField(max_length=20,blank=False)
    before_date = models.DateField()
    trip_object =  models.ForeignKey(Trip ,blank=True,null=True,default=None,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)  

class ShipmentItem(models.Model):
    shipment_id = models.ForeignKey(Shipment,on_delete=models.CASCADE)
    item_link = models.URLField()
    item_name = models.CharField(max_length=100)
    item_weight = models.FloatField(
        validators=[
            MinValueValidator(limit_value=0.0, message="enter valid weight."),
            MaxValueValidator(limit_value=100.0, message="Item weight cannot exceed 100.0.")
        ]
    )   
    single_item_price = models.DecimalField(max_digits=8, decimal_places=2)
    rate = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    item_image = models.ImageField(null=True, blank=True)


 # hn3ml signal 3shan n3ml price w 3shan y3ml item quentity
    #a3mlo bilpostgres