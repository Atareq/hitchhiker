from django.shortcuts import render
from .models import Trip
from .serializers import TripSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filter import TripFilters
from rest_framework.decorators import api_view

# @api_view(['GET'])
# def MyTripViewSet(request):

#     pass    



