from rest_framework import generics, permissions, status ,viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
from django.contrib.auth.hashers import check_password
import phonenumbers
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from User_auth.models import CustomUser
from info_from_token import get_user_pk_from_token


class UserRegistrationView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny,]

    def check_phone(self, string_phone_number):
        try:
            phone_number = phonenumbers.parse(string_phone_number, None)
            if phonenumbers.is_possible_number(phone_number):
                return True
        except:
            return False

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        string_phone_number = request.data.get('phone_number')
        valid_phone_number = self.check_phone(string_phone_number)
        
        if not valid_phone_number:
            return Response("Check the phone number you entered!", status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        refresh = RefreshToken.for_user(user)
        
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        
        return Response({
            'data': serializer.data,
        }, status=status.HTTP_201_CREATED)

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        
        user = CustomUser.objects.filter(Q(username=username) | Q(phone_number=username)).first()
        
        if user and check_password(password, user.password):
            refresh = RefreshToken.for_user(user)
            
            data = {
                
                "access": str(refresh.access_token),
            }
            
            return Response(data, status=status.HTTP_200_OK)
        
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self,request):
        user_pk = get_user_pk_from_token(request)
        user_data=CustomUser.objects.get(id=user_pk)
        user_serialized = UserRegistrationSerializer(instance=user_data)
        return Response(user_serialized.data,status=status.HTTP_200_OK)