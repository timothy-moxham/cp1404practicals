"""
CP1404/CP5632 Practical
Program to test taxi class
"""

from taxi import Taxi


def main():
    """Test taxi class"""
    my_taxi = Taxi("Prius 1", 100)

    my_taxi.drive(40)
    print(f"{my_taxi}, Fare: ${my_taxi.get_fare()}")

    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, Fare: ${my_taxi.get_fare()}")


main()
