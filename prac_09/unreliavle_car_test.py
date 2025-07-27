"""
Test program for UnreliableCar class
"""

from unreliable_car import UnreliableCar

def test_unreliable_cars():
    """Demonstrate how UnreliableCar behaves with different reliability levels."""
    reliable_car = UnreliableCar("Reliable One", 100, 90)
    unreliable_car = UnreliableCar("Sketchy Ride", 100, 9)

