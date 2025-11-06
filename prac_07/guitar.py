"""
CP1404/CP5632 Practical
Guitar class
Estimate: 5 minutes
Actual: 6 minutes
"""

CURRENT_YEAR = 2025


class Guitar:
    """Represent information about guitars."""

    def __init__(self, name="", year=0, cost=0):
        """Initiate a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        """Calculate the age of a guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage."""
        return self.get_age() >= 50
