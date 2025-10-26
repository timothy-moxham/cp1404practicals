"""
CP1404/CP5632 Practical
Program to read, process, and display information from Wimbledon gentlemen's single champions csv file
Estimate: 30 minutes
Actual: 31 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Load, process, and display records from a Wimbledon's csv data file."""
    records = load_records(FILENAME)
    champion_to_number_of_wins, countries_of_champions = process_records(records)
    display_results(champion_to_number_of_wins, countries_of_champions)


def display_results(champion_to_number_of_wins, countries_of_champions):
    """Display results of Wimbledon champions and countries of champions."""
    print("Wimbledon Champions: ")
    for champion, number_of_wins in champion_to_number_of_wins.items():
        print(champion, number_of_wins)

    print(f"\nThese {len(countries_of_champions)} countries have won Wimbledon:")
    print(", ".join(sorted(countries_of_champions)))


def process_records(records):
    """Process records of Wimbledon champions and countries of champions."""
    champion_to_number_of_wins = {}
    countries_of_champions = set()
    for record in records:
        champion_to_number_of_wins[record[2]] = champion_to_number_of_wins.get(record[2], 0) + 1
        countries_of_champions.add(record[1])
    return champion_to_number_of_wins, countries_of_champions


def load_records(filename):
    """Load csv file of Wimbledon data and return it as a list."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        records = [line.strip().split(",") for line in in_file]
    return records


main()
