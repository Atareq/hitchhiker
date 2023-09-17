from rest_framework.response import Response
from rest_framework import viewsets 
from .models import Trip
from .serializers import TripSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from .filter import TripFilters


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TripFilters

    def get_queryset(self):
        query = self.queryset

        if self.action == 'list' and self.request.query_params.get('date'):
            import datetime
            query = query.filter(date__range=[
                datetime.date.today(),
                self.request.query_params.get('date')
            ])
        return query
