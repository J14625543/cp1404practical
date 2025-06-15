import random

LINE_NUMBERS = 6
NUMBERS_MINIMUM = 1
NUMBERS_MAXIMUM = 45

def main():
    while True:
        try:
            number = int(input("How many quick picks: "))
            if number > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for i in range(number):
        quick_picks = []
        while len(quick_picks) < LINE_NUMBERS:
            new_number = random.randint(NUMBERS_MINIMUM, NUMBERS_MAXIMUM)
            if new_number not in quick_picks:
                quick_picks.append(new_number)
        quick_picks.sort()
        print(" ".join(f"{num:2}" for num in quick_picks))

main()
