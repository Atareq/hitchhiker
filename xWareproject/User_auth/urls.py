
from django.urls import path
from User_auth.genericapi import UserRegistrationView,UserLoginView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('register/', UserRegistrationView.as_view()),

    path('notifications/<int:pk>/', UserLoginView.as_view()),

    path('auth/token/login', TokenObtainPairView.as_view()),

  
]
