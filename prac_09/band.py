"""
CP1404/CP5632 Practical
Band class
"""


class Band:
    """Band class for storing details of a band."""

    def __init__(self, name):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band"""
        return f"{self.name} ({", ".join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Append a musician to the band musicians list."""
        return self.musicians.append(musician)

