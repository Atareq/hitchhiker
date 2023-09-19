from django.db import models
from User_auth.models import CustomUser
from django.core.validators import MaxValueValidator ,MinValueValidator


cities_of_travel =[('usa','United Status America'),
('ca','canada'),('kwt','kewit'),('egy','egypt'),
('ksa','saudi')]
class Trip(models.Model):
    user_t=models.ForeignKey(CustomUser, null=False,on_delete=models.CASCADE )
    location_from =models.CharField(choices = cities_of_travel,max_length=10)
    location_to =models.CharField(choices = cities_of_travel,max_length=10)
    date = models.DateField()
    price = models.DecimalField(null=True,max_digits=8, decimal_places=2)
    weight_available =  models.FloatField()
    rate = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    notes = models.CharField(max_length=1000)
