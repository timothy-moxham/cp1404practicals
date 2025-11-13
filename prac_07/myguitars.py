"""
CP1404/CP5632 Practical
Program to process guitar records, get new guitar records, and save new records to a file.
"""

from guitar import Guitar

FILE = "guitars.csv"


def main():
    """Process guitar records, get new guitar records, and save new records to a file."""
    guitars = process_guitar_records(FILE)
    guitars = get_guitar_records(guitars)

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    save_guitar_records(FILE, guitars)


def save_guitar_records(file, guitars):
    """Save guitar records to a file."""
    with open(FILE, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def get_guitar_records(guitars):
    """Get guitar records from user and add it to a list."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{Guitar(name, year, cost)} added.")
        name = input("Name: ")
    return guitars


def process_guitar_records(file):
    """Process records from a file containing guitar information."""
    guitars = []
    with open(file, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


main()
