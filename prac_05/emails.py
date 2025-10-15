"""
CP1404/CP5632 Practical
Program to store users' emails and names
Estimate: 20 minutes
Actual: 17 minutes
"""


def main():
    """Get user's email and name and store it in a dictionary."""
    email = input("Email: ")
    email_to_name = {}
    while email != "":
        name = extract_name_from_email(email)
        response = input(f"Is your name {name}? (Y/n) ").upper()
        if response != "Y" and response != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract a name from an email."""
    return " ".join(email[:email.find("@")].split(".")).title()


main()
