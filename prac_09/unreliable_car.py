"""
Unreliable Car class for CP1404 Practical 9
"""

from random import randint
from car import Car


class UnreliableCar(Car):
    """Unreliable car that may or may not drive based on reliability percentage."""

    def __init__(self, name: str, fuel: float, reliability: int):
        """Initialize unreliable car with name, fuel and reliability (1-100)."""
        super().__init__(name, fuel)
        self.reliability = reliability  # reliability percentage (1-100)
