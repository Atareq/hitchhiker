import django_filters
from django.db import models
from datetime import date
from .models import Trip 
from datetime import datetime, timedelta


class TripFilters(django_filters.FilterSet):
    location_from = django_filters.CharFilter(lookup_expr='iexact')
    location_to = django_filters.CharFilter(lookup_expr='iexact')
    date = django_filters.DateFilter(lookup_expr='lt')    
    # Calculate today's date
    today = datetime.now().date()
    # Calculate the future date, in this case, 'end_date'
    end_date = date(2023, 12, 31)  # Replace this with your desired future date

    # Use the __range lookup to filter records
    result = MyModel.objects.filter(my_date_field__range=(today, end_date))

    # 'result' now contains records where 'my_date_field' is between today and 'end_date'

    class Meta:
        model = Trip
        fields = ['location_from','location_to','date']