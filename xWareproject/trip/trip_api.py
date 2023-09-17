from rest_framework.response import Response
from rest_framework import viewsets 
from .models import Trip
from django_filters.rest_framework import DjangoFilterBackend
from .filter import TripFilters
from .serializers import TripSerializer
from info_from_token import get_user_pk_from_token
from rest_framework import status
from rest_framework.decorators import api_view


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
    


@api_view(['GET'])
def  mytrip_view_set(request):
    user_pk = get_user_pk_from_token(request=request)
    my_trips_objects = Trip.objects.filter(user_t=user_pk)
    serialized_trip = TripSerializer(my_trips_objects, many=True)
    mytrips_data = serialized_trip.data
    return Response(mytrips_data, status=status.HTTP_200_OK)