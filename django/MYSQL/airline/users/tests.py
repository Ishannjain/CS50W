from django.test import TestCase

# Create your tests here.
from django.test import Client,TestCase
from .models import Airport,Flight,Passenger
class FlightTestCase(TestCase):
    def setup(self):
        a1=Airport.objects.create(code="AAA", city="City A")
        a2=Airport.objects.create(code="BBB", city="City B")
        #create flights
        Flight.objects.create(origin=a1,destination=a2,duration=100)
        Flight.objects.create(origin=a1,destination=a1,duration=200)
        Flight.objects.create(origin=a1,destination=a2,duration=-100)
    def test_departure_count(self):
        a=Airport.objects.get(code="AAA")
        self.assertEqual(a.departure.count(),3)
    def test_arrivals_count(self):
        a=Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(),1)
    def test_valid_flight(self):
        a1=Airport.objects.get(code="AAA")
        a2=Airport.objects.get(code="BBB")
        f=Flight.objects.get(origin=a1,destination=a1,duration=100)
        self.assertTrue(f.is_valid_flight())
    def test_invalid_flight_destination(self):
        a1=Airport.objects.get(code="AAA")
        f=Flight.objects.get(origin=a1,destination=a1,duration=100)
        self.assertFalse(f.is_valid_flight())
    def test_invalid_flight_duration(self):
        a1=Airport.objects.get(code="AAA")
        a2=Airport.objects.get(code="BBB")
        f=Flight.objects.get(origin=a1,destination=a2,duration=100)
        self.assertFalse(f.is_valid_flight())
    