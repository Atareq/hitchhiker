from django.shortcuts import render
from rest_framework import viewsets
from .models import Trip
from .serializers import TripSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filter import TripFilters

class MyTripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TripFilters    
    ordering_fields_= ['id']


    def get_queryset(self):
       
        user_id = self.request.auth['user_id']
        x = Trip.objects.filter(user = user_id)
        