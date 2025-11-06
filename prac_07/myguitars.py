"""
CP1404/CP5632 Practical

"""

from guitar import Guitar

FILE = "guitars.csv"


def main():
    """"""
    guitars = process_guitar_records(FILE)
    guitars.sort()

    for guitar in guitars:
        print(guitar)


def process_guitar_records(file):
    guitars = []
    with open(file, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


main()
