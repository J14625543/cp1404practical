"""
Vehicle class for CP1404 Practical 9
Simulates a simple car with fuel and distance tracking.
"""


class Vehicle:
    """A basic vehicle model with fuel usage and distance record."""

    def __init__(self, model_name="", initial_fuel=0):
        """
        Create a new Vehicle instance.

        Args:
            model_name (str): name of the vehicle
            initial_fuel (float): starting amount of fuel
        """
        self.model_name = model_name
        self.fuel_level = initial_fuel
        self.distance_travelled = 0


