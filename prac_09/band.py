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