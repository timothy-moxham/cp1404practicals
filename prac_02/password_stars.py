"""
CP1404/CP5632 - Practical
Program to get a valid password and print it as asterisks
"""

MINIMUM_LENGTH = 5


def main():
    """Get and print password as asterisks."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def print_asterisks(text):
    """Print text as asterisks."""
    print(len(text) * "*")


def get_password(minimum_length):
    """Get a password that meets a minimum length."""
    password = input("Password: ")
    while len(password) < minimum_length:
        print(f"Error: Password must be at least {minimum_length} characters")
        password = input("Password: ")
    return password


main()
