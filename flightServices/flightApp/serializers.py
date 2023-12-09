from rest_framework import serializers
from flightApp.models import Flight,Passenger,Reservation
import re

# Adding Validation
'''def Validate_flightNumber(self,flightNumber):
    if(re.match("^[a-zA-zo-a]*$",flightNumber)==None):
        raise serializers.ValidationError("Invalid flight number make sure it is Alphanumeric")
    return flightNumber
'''

# Adding Custome Validation


def validate(self,data):
    print("Validation")
    print(data['flightNumber'])
    return data

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'