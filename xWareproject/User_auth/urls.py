
from django.urls import path , include
from User_auth.genericapi import UserRegistrationView,UserLoginView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'register', UserRegistrationView, basename='register')

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', UserLoginView.as_view()),

]
