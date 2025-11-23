"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi class that includes a 'fanciness' attribute and fixed flagfall fee."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = fanciness * Taxi.price_per_km

    def __str__(self):
        """Return a string representation like Taxi but with flagfall fee."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the Silver Service Taxi trip."""
        return super().get_fare() + self.flagfall
