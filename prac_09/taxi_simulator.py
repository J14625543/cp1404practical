"""
Taxi Simulator for CP1404 Practical 9
"""

from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU_OPTIONS = "q)uit, c)hoose taxi, d)rive"

def taxi_simulator():
    """Run the taxi simulator."""
    total_cost = 0
    fleet = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    selected_taxi = None

    print("Welcome to the Taxi Simulator!")
    print(MENU_OPTIONS)

