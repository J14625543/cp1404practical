"""
Demo for using SilverServiceTaxi class
"""

from silver_service_taxi import SilverServiceTaxi


def demo_silver_taxi():
    """Demonstrate SilverServiceTaxi usage."""
    fancy_taxi = SilverServiceTaxi(name="Demo Silver Taxi", fuel=100, fanciness=2)
    fancy_taxi.drive(distance=18)

    print(fancy_taxi)
    fare = fancy_taxi.get_fare()
    print(f"Fare for the trip: ${fare:.2f}")


if __name__ == "__main__":
    demo_silver_taxi()

