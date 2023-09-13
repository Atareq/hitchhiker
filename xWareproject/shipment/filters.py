import django_filters
from .models import Shipment,ShipmentItem

class ShipmentFilters (django_filters.FilterSet):
    from_location = django_filters.CharFilter(lookup_expr='exact')
    to_location = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Shipment 
        fields = []


class ShipmentItemFilters(django_filters.FilterSet):

    item_weight = django_filters.NumberFilter(lookup_expr='lt')


    class Meta:
        model = ShipmentItem
        fields = []