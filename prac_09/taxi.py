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

    def __str__(self):
        """Return string representation including fare distance and rate."""
        base_str = super().__str__()
        return f"{base_str}, fare distance: {self.fare_distance} km, rate: ${self.rate_per_km:.2f}/km"

    def calculate_fare(self):
        """Compute total fare for the current trip."""
        return self.rate_per_km * self.fare_distance

    def begin_fare(self):
        """Reset fare distance for a new trip."""
        self.fare_distance = 0

    def drive(self, distance):
        """Drive the taxi and update fare distance accordingly."""
        actual_distance = super().drive(distance)
        self.fare_distance += actual_distance
        return actual_distance

