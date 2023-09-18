# serializers.py
from rest_framework import serializers , permissions
from django.contrib.auth import get_user_model
from .models import CustomUser
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
  
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'phone_number')

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(required=False)
    