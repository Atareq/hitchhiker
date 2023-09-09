<<<<<<< HEAD:xWareproject/User_auth/urls.py
# urls.py
from django.urls import path
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
=======
from django.urls import path
from Users.api import UserRegisterViewset, TokenView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('register/', UserRegisterViewset.as_view({'post': 'create'})),

    path('notifications/<int:pk>/', UserRegisterViewset.as_view({'get': 'retrieve','patch': 'partial_update','delete': 'destroy'})),

    path('auth/token/login', TokenObtainPairView.as_view()),

    path('jnds/koko/', TokenObtainPairView.as_view()),
>>>>>>> origin/main:xWareproject/Users/urls.py
]
