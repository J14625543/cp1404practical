"""
LuxuryTaxi class for CP1404 Practical 9
Represents a premium taxi with a flagfall fee.
"""

from taxi import Taxi


class LuxuryTaxi(Taxi):
    """A premium taxi that includes an extra flagfall fee."""

    BASE_FLAGFALL = 4.5

    def __init__(self, label, fuel_amount, luxury_level):
        """Create a LuxuryTaxi instance with given name, fuel, and luxury multiplier."""
        super().__init__(label, fuel_amount)
        self.luxury_multiplier = luxury_level
        self.price_per_km *= self.luxury_multiplier

    def __str__(self):
        """Return formatted string showing taxi details and flagfall."""
        parent_str = super().__str__()
        return f"{parent_str} | includes flagfall ${self.BASE_FLAGFALL:.2f}"

    def calculate_fare(self):
        """Return total fare including flagfall."""
        base_fare = super().get_fare()
        return base_fare + self.BASE_FLAGFALL
