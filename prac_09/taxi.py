"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.car import Car


class Taxi(Car):
    """A specialized Car that tracks fare distance and calculates fare cost."""

    def __init__(self, model, fuel_amount, rate_per_km):
        """Initialize Taxi using Car's init and add fare-specific attributes."""
        super().__init__(model, fuel_amount)
        self.rate_per_km = rate_per_km
        self.fare_distance = 0



