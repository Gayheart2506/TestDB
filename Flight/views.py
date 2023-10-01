from django.shortcuts import render
from .models import Flight

# Create your views here.


def index(request):
    return render(request, "flight/index.html", {
        "Flights": Flight.objects.all(),
    })


def flight(request, flight_id):
    flights = Flight.objects.get(pk=flight_id)
    return render(request, "flight/flights.html", {
        "flights": flights,
        "passengers": flights.passengers.all(),
    })


def book(request, flight_id):
    if request.method == "POST":
        flights = Flight.object.get(pk=flight_id)
        passenger = 
