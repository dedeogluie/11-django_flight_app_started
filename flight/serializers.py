from rest_framework import serializers
from .models import Flight, Passenger, Rezervation

class FlightSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Flight
        fields = "__all__"
        
class RezervationSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Rezervation
        fields = "__all__"
        

class PassengerSerializer(serializers.ModelSerializer):
    
    class Meta :
        model =Passenger
        fields = "__all__"