"""
CP1404/CP5632 - Practical
Program to get a valid password and print it as asterisks
"""

MINIMUM_LENGTH = 5


def main():
    """Get and print password as asterisks."""
    password = get_password()
    print_asterisks(password)


def print_asterisks(text):
    """Print text as asterisks."""
    print(len(text) * "*")


def get_password():
    """Get a password that meets a minimum length."""
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Error")
        password = input("Password: ")
    return password


main()
