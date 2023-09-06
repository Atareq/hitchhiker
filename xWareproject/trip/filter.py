import django_filters
from .models import Trip 


class TripFilters(django_filters.FilterSet):
    location_from = django_filters.CharFilter(lookup_expr='iexact')
    location_to = django_filters.CharFilter(lookup_expr='iexact')
    date = django_filters.DateTimeFilter(lookup_expr='lt')

    class Meta:
        model = Trip
        fields = ['location_from','location_to','date']