"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_details = load_subject_details(FILENAME)
    display_subject_details(subject_details)


def display_subject_details(subject_details: list):
    for record in subject_details:
        print(f"{record[0]} is taught by {record[1]} and has {record[2]} students")


def load_subject_details(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject.append(parts)
    input_file.close()
    return subject


main()
