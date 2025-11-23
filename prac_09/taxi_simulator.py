"""
CP1404/CP5632 Practical
Program to simulate taxis
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Menu for taxi simulator program."""
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Get an index for a corresponding list of taxis, and return that taxi in the list."""
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        return taxis[taxi_choice]
    except (ValueError, IndexError):
        print("Invalid taxi choice")


def display_taxis(taxis):
    """Display each taxi in a list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(taxi):
    """Get distance to drive taxi, and return the fare of that trip."""
    distance = int(input("Drive how far? "))
    if distance > taxi.fuel:
        distance = taxi.fuel
    taxi.start_fare()
    taxi.drive(distance)
    fare = taxi.get_fare()
    print(f"Your {taxi.name} will cost you ${fare:.2f}")
    return fare


main()
