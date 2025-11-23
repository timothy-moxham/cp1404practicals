"""
CP1404/CP5632 Practical
Program to test Taxi class
"""

from taxi import Taxi


def main():
    """Test taxi class."""
    my_taxi = Taxi("Prius 1", 100, 1.23)

    distance = my_taxi.drive(40)
    print(f"{my_taxi}, Fare: ${my_taxi.get_fare()}, expected ${distance * my_taxi.price_per_km}")

    my_taxi.start_fare()
    my_taxi.drive(100)
    # Unexpected result due to fuel
    print(f"{my_taxi}, Fare: ${my_taxi.get_fare()}, expected ${distance * my_taxi.price_per_km}")


main()
