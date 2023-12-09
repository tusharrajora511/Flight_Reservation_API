from django.shortcuts import render
from flightApp.models import Flight,Passenger,Reservation
from flightApp.serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


# Create your views here.
@api_view(['POST'])
def find_flights(request):
    flights = flights.objects.Filter(departureCity = request.data['departurCity'],arrivalCity = request.data['arrivalCity'],dateofDeparture = request.data['dateofDeparture'])
    serializer = FlightSerializer(flights,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['FlightId'])
    passenger =Passenger()

    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.passportNumber = request.data['passportNumber']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    reservation.save(reservation)
    return Response(status=status.HTTP_201_CREATED)




class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]