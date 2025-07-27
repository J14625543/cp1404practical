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

    choice = input("Select an option: ").lower()
    while choice != 'q':
        if choice == 'c':
            print("Available taxis:")
            list_taxis(fleet)
            try:
                taxi_index = int(input("Select taxi by number: "))
                selected_taxi = fleet[taxi_index]
            except (ValueError, IndexError):
                print("That is not a valid taxi choice.")
        elif choice == 'd':
            if selected_taxi:
                selected_taxi.start_fare()
                try:
                    distance = float(input("Enter distance to drive: "))
                    selected_taxi.drive(distance)
                    fare = selected_taxi.get_fare()
                    print(f"Trip cost for {selected_taxi.name}: ${fare:.2f}")
                    total_cost += fare
                except ValueError:
                    print("Please enter a valid number for distance.")
            else:
                print("Please choose a taxi first before driving.")
        else:
            print("Invalid option selected.")

        print(f"Total bill so far: ${total_cost:.2f}")
        print(MENU_OPTIONS)
        choice = input("Select an option: ").lower()

    print(f"Final total cost: ${total_cost:.2f}")
    print("Current taxis in the fleet:")
    list_taxis(fleet)



