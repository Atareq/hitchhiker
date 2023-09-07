# views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  
import bcrypt

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Hash the password before saving the user
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()

        refresh = RefreshToken.for_user(user)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):

        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response(data, status=status.HTTP_200_OK)










# # Step 1: Generate a salt
# salt = bcrypt.gensalt()

# # Step 3: Collect the user's password (plaintext)
# user_password = "user123password"

# # Step 4: Combine the password and salt
# password_with_salt = user_password.encode('utf-8') + salt

# # Step 5: Hash the password
# hashed_password = bcrypt.hashpw(password_with_salt, salt)

# # Step 6: Store the salt and hashed password in the database
# # You should also store the user's unique identifier (e.g., username or email) for later retrieval
# store_salt_and_hash_in_database(salt, hashed_password)
