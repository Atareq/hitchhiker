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
    def retrieve(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        date = request.date
        print(date)
        return Response(serializer.data)
#     start_date = date.today()

# events_in_january = Trip.objects.filter(start_date__range=(start_date, end_date))
#   def date(self):
#         l_date = request.data.date 
 