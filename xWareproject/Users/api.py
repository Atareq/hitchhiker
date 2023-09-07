import jwt
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets , filters
from rest_framework.views import APIView
from Users.models import Userinfo
from Users.serializers import UserRegisterSerializer
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from Users.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from django.contrib.auth import authenticate
from rest_framework.exceptions import NotFound, APIException
from rest_framework.response import Response


class UserRegisterViewset(viewsets.ModelViewSet):
    queryset=Userinfo.objects.all()
    serializer_class=UserRegisterSerializer


class UserLoginViewset(viewsets.ModelViewSet):
    queryset=Userinfo.objects.all()
    serializer_class=UserRegisterSerializer   
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class TokenView(APIView):
    def post(self, request: Request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(
                username=username,
                password=password)
            if not user:
                raise NotFound()

            token = jwt.encode(
                {'user_id': user.pk},
                settings.SECRET_KEY,
                algorithm="HS256")

            return Response({'token': token})
        except:
            raise APIException
