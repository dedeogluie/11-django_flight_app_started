from django.shortcuts import render

from .serializers import FlightSerializer ,RezervationSerializer ,PassengerSerializer

from .models import Flight,Passenger,Rezervation

from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from .permissions import IsStaffOrReadOnly

from datetime import datetime


# Create your views here.

class FlightListCreate(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    # permission_classes = [IsAuthenticated,IsStaffOrReadOnly]


class RezervationListCreate(generics.ListCreateAPIView):
    queryset = Rezervation.objects.all()
    serializer_class = RezervationSerializer
    permission_classes = [IsAuthenticated,IsStaffOrReadOnly]
    
    
class PassengerListCreate(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated,IsStaffOrReadOnly]
    

class FlightUptadeDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated,IsStaffOrReadOnly]
    
    
class PassengerUptadeDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset= Passenger.objects.all()
    serializer_class= PassengerSerializer
    permission_classes = [IsAuthenticated,IsStaffOrReadOnly]
    
    
class FlightListView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_staff :
            return Flight.objects.all()
        
        return Flight.objects.filter(date_of_departure__gte =datetime.today())  
    #__gte: Bu, filtreleme işleminin türünü belirleyen bir operatördür. "gte" operatörü, "greater than or equal to" ifadesinin kısaltmasıdır ve Türkçe'de "büyük veya eşit" anlamına gelir. 