from datetime import date
import django_filters
import datetime
from .models import Trip 


class TripFilters(django_filters.FilterSet):
    location_from = django_filters.CharFilter(lookup_expr='iexact')
    location_to = django_filters.CharFilter(lookup_expr='iexact')
    weight_available = django_filters.NumberFilter(lookup_expr='gte')
    
    class Meta:
        model = Trip
        fields = ['location_from', 'location_to']

