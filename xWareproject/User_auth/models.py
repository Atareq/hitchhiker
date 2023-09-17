from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import status 
from rest_framework.response import Response
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15,unique=True,blank=False)
    first_name = models.CharField(("first name"), max_length=150,blank=False)
    last_name = models.CharField(("last name"), max_length=150,blank=False)
    email = models.EmailField(("email address"),unique=True,blank=False)
