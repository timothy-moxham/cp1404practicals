"""
CP1404/CP5632 Practical
Program to test Guitar class
Estimate: 10 minutes
Actual: 7 minutes
"""

from guitar import Guitar

gibson_l5_ces = Guitar("Gibson L-5 CES", 1951, 20000)
another_guitar = Guitar("Another Guitar", 2013, 150)

print(f"{gibson_l5_ces.name} get_age() - Expected 74. Got {gibson_l5_ces.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 12. Got {another_guitar.get_age()}")
print(f"{gibson_l5_ces.name} is_vintage() - Expected True. Got {gibson_l5_ces.is_vintage()}")
print(f"{gibson_l5_ces.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
