from rest_framework.response import Response
from rest_framework import viewsets 
from .models import Trip
from .serializers import TripSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from .filter import TripFilters
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import viewsets
from .models import Trip
from .serializers import TripSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filter import TripFilters
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import TripSerializer
from rest_framework.decorators import api_view
from info_from_token import get_user_pk_from_token
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Trip
from .serializers import TripSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filter import TripFilters
from rest_framework.decorators import api_view
from info_from_token import get_user_pk_from_token
from rest_framework.response import Response
from rest_framework import viewsets 
from .models import Trip
from django_filters.rest_framework import DjangoFilterBackend
from .filter import TripFilters
from .serializers import TripSerializer
from info_from_token import get_user_pk_from_token
from rest_framework import status
from rest_framework.decorators import api_view


class TripViewSet(viewsets.ModelViewSet):
    
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TripFilters
    permission_classes=[IsAuthenticated]
 
    def get_queryset(self):
        query = self.queryset

        if self.action == 'list' and self.request.query_params.get('date'):
            import datetime
            query = query.filter(date__range=[
                datetime.date.today(),
                self.request.query_params.get('date')
            ])
        return query
    def create(self, request, *args, **kwargs):
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
        return Response (tripSerializer.data, status=status.HTTP_201_CREATED)

    def  mytrip(self,request):
        print("taaaaareq     "*100)
        user_pk = get_user_pk_from_token(request=request)
        my_trips_objects = Trip.objects.filter(user_t=user_pk)
        serialized_trip = TripSerializer(my_trips_objects, many=True)
        return Response(serialized_trip.data, status=status.HTTP_200_OK)


