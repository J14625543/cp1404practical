MINIMUM_LENGTH = 6

def main():
    """Main function to get password and display it as asterisks."""
    password = get_password()
    asterisks(password)

def get_password():
    """Prompt the user until a valid password is entered, then return it."""
    password = input(f"Enter your password with at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter your password with at least {MINIMUM_LENGTH} characters: ")
    return password

def asterisks(password):
    """Print asterisks equal to the length of the password."""
    print('*' * len(password))

main()
