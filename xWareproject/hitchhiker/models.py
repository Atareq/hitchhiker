from django.db import models
cities_of_travel =[('usa','United Status America'),
    ('ca','canada'),('kwt','kewit'),('egy','egypt'),
    ('ksa','saudi')]
class Trip (models.Model):
    max_avai_weight= models.SmallIntegerField()
    from_trip =models.CharField(choices = cities_of_travel)
    to_trip = models.CharField(choices = cities_of_travel)
    trip_date = models.DateField()






class Shipments (models.Model):
   
    item_link = models.URLField(max_length=200)
    weight = models.SmallIntegerField()
    from_ship =models.CharField(choices = cities_of_travel)
    to_ship = models.CharField(choices = cities_of_travel)
    ship_date = models.DateField()


# Create your models here.
