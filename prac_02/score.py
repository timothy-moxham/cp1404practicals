"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import uniform


def main():
    """Get and print the status of score."""
    score = float(input("Enter score: "))
    score_status = determine_status(score)
    print(f"Score of {score:.2f}: {score_status}")

    random_score = round(uniform(0, 100), 2)
    score_status = determine_status(random_score)
    print(f"Score of {random_score:.2f}: {score_status}")


def determine_status(score):
    """Determine the status of a score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
