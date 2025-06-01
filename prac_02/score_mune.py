MENU = "(G)et a valid score, (P)rint result, (S)how stars, (Q)uit"
print(MENU)

def main():
    """Main menu loop to interact with the user."""
    score = get_valid_score()
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid input, please choose from the menu.")
        print(MENU)
        choice = input("Enter your choice: ").upper()
    print("Farewell")

def get_valid_score():
    """Prompt user for a score between 0 and 100 (inclusive)."""
    score = int(input("Enter your score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! Score must be between 0 and 100.")
        score = int(input("Enter your score (0-100): "))
    return score

def print_result(score):
    """Print result category based on score value."""
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def show_stars(score):
    """Print stars representing the score."""
    print("*" * int(score))

main()


