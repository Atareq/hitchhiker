from django.urls import path , include
from User_auth.api import UserRegistrationView,UserLoginView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'register', UserRegistrationView, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginView.as_view()),

]
