"""
CP1404/CP5632 Practical
ProgrammingLanguage class
"""


class ProgrammingLanguage:
    """Represent information about programming languages."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the typing of a programming language is dynamic."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of a programming language."""
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"
