from django.db import models
from django.contrib.auth.models import User


class Trip(models.Model):
    cities_of_travel =[('usa','United Status America'),
    ('ca','canada'),('kwt','kewit'),('egy','egypt'),
    ('ksa','saudi')]
    title = models.CharField(max_length=200)
    location_from =models.CharField(choices = cities_of_travel,max_length=10)
    location_to =models.CharField(choices = cities_of_travel,max_length=10)
    date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight_available =  models.FloatField()

