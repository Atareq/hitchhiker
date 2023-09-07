from rest_framework import serializers
from .models import Userinfo
from django.contrib.auth import get_user_model, authenticate

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model= Userinfo
        fields='__all__'
    
