MENU = "C = Celsius converts to Fahrenheit \nF = Fahrenheit to Celsius \nQ = Quit"
print(MENU)


def main():
    """Main program loop to convert temperatures between Celsius and Fahrenheit."""
    choice = input("Choose >>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")

        print(MENU)
        choice = input("Choose >>> ").upper()

    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Parameters:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    Parameters:
        fahrenheit (float): Temperature in degrees Fahrenheit.

    Returns:
        float: Temperature in degrees Celsius.
    """
    return 5 / 9 * (fahrenheit - 32)


main()
