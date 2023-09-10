import django_filters
from django.db import models
from datetime import date
from .models import Trip 
from datetime import datetime, timedelta


class TripFilters(django_filters.FilterSet):
    location_from = django_filters.CharFilter(lookup_expr='iexact')
    location_to = django_filters.CharFilter(lookup_expr='iexact')
  
    class Meta:
        model = Trip
        fields = ['location_from','location_to','date']