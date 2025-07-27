"""
Demo for using SilverServiceTaxi class
"""

from silver_service_taxi import SilverServiceTaxi


def demo_silver_taxi():
    """Demonstrate SilverServiceTaxi usage."""
    fancy_taxi = SilverServiceTaxi(name="Demo Silver Taxi", fuel=100, fanciness=2)
    fancy_taxi.drive(distance=18)


