class Car:
    def __init__(self, fuel=0):
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
            self.fuel += amount

