"""
CP1404/CP5632 Practical
Project class
"""


class Project:
    """Represent information about projects."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initiate a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, "
                f"estimate ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Determine if the priority level of a Project is less than another Project."""
        return self.priority < other.priority

    def __get__(self, other):
        """Determine if the start date of a Project is greater than or equal to another Project."""
        return self.start_date >= other.start_date
