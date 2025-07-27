"""
Test program for UnreliableCar class
"""

from unreliable_car import UnreliableCar

def test_unreliable_cars():
    """Demonstrate how UnreliableCar behaves with different reliability levels."""
    reliable_car = UnreliableCar("Reliable One", 100, 90)
    unreliable_car = UnreliableCar("Sketchy Ride", 100, 9)

    # Try to drive both cars from 1km to 11km
    for distance in range(1, 12):
        print(f"Trying to drive {distance} km:")
        result1 = reliable_car.drive(distance)
        result2 = unreliable_car.drive(distance)
        print(f"{reliable_car.name:<15} drove {result1:>2} km")
        print(f"{unreliable_car.name:<15} drove {result2:>2} km")

    # Print final states of both cars
    print("\nFinal status:")
    print(reliable_car)
    print(unreliable_car)

if __name__ == "__main__":
    test_unreliable_cars()
