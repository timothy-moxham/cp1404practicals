"""
CP1404/CP5632 Practical
Program to calculate the information of 5 numbers prompted from a user.
"""

from random import randint

RANDOM_NUMBERS_PER_LINE = 6
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))

for line in range(number_of_quick_picks):
    random_numbers = []
    for number in range(RANDOM_NUMBERS_PER_LINE):
        random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        while random_number in random_numbers:
            random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        random_numbers.append(random_number)
    random_numbers.sort()
    print(" ".join(f"{number:2}" for number in random_numbers))
