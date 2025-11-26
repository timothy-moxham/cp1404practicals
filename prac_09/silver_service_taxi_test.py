"""
CP1404/CP5632 Practical
Program to test SilverServiceTaxi class
"""

from silver_service_taxi import SilverServiceTaxi

KNOWN_VALUE = 48.80


def main():
    """Test SilverServiceTaxi class."""
    premium_taxi = SilverServiceTaxi("Premium Taxi", 18, 2)
    premium_taxi.drive(18)
    assert premium_taxi.get_fare() == KNOWN_VALUE  # No AssertionError raised with known, expected value


main()
