from django.db import models
from User_auth.models import CustomUser


class Trip(models.Model):
    user_s=models.ForeignKey(CustomUser, null=True,on_delete=models.CASCADE )
    cities_of_travel =[('usa','United Status America'),
    ('ca','canada'),('kwt','kewit'),('egy','egypt'),
    ('ksa','saudi')]
    title = models.CharField(max_length=200)
    location_from =models.CharField(choices = cities_of_travel,max_length=10)
    location_to =models.CharField(choices = cities_of_travel,max_length=10)
    date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight_available =  models.FloatField()

