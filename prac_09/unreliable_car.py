"""
CP1404/CP5632 Practical
UnreliableCar class
"""

from car import Car
from random import randint


class UnreliableCar(Car):
    """Represent a version of a Car that includes a chance-based drive method."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car based on chance."""
        if randint(0, 100) >= self.reliability:
            distance = 0
        return super().drive(distance)
