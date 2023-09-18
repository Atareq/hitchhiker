from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import TripSerializer
from rest_framework.decorators import api_view
from info_from_token import get_user_pk_from_token


@api_view(['POST'])
def add_trip(request):
    trip_data = request.data
    try:
        user_pk = get_user_pk_from_token(request=request)
    except:
        if user_pk is None:
            return Response({"error": "Please log in again"}, status=status.HTTP_401_UNAUTHORIZED)

    trip_data["user_t"] =user_pk
    tripSerializer = TripSerializer(data=trip_data)
    tripSerializer.is_valid(raise_exception=True)
    tripSerializer.save()
    return Response (trip_data,status=status.HTTP_201_CREATED)


