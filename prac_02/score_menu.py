"""
CP1404/CP5632 - Practical
Menu-driven program to determine score status
"""

MENU = "(G)et score, (P)rint result, (S)how stars, (Q)uit"


def main():
    """Menu-driven program to determine score status and other features."""
    score = get_valid_score()
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            score_status = determine_status(score)
            print(f"Score of {score:.2f}: {score_status}")
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input("Choice: ").upper()
    print("Goodbye.")


def get_valid_score():
    """Get a score that is between 0 and 100 inclusive."""
    score = float(input("Score: "))
    while score < 0 or score > 100:
        print("Error: Score must be between 0 and 100")
        score = float(input("Score: "))
    return score


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
