import django_filters
from .models import Shipment

class ShipmentFilters (django_filters.FilterSet):
    from_location = django_filters.CharFilter(lookup_expr='exact')
    to_location = django_filters.CharFilter(lookup_expr='exact')
    before_date = django_filters.DateTimeFilter(lookup_expr='lt')

    class Meta:
        model = Shipment
        fields = []

