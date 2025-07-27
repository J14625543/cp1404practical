"""
Test program for Taxi class
"""

from taxi import Taxi

def run_taxi_demo():
    """Demonstrate Taxi class usage."""
    taxi_instance = Taxi("Prius 1", 100)
    taxi_instance.drive(40)
    print(taxi_instance)
    taxi_instance.start_fare()
    taxi_instance.drive(100)
    print(taxi_instance)

if __name__ == "__main__":
    run_taxi_demo()
