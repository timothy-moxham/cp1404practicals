"""

Estimate: 60 minutes
Actual:
"""

from project import Project

MENU = """- (L)oad projects
- (S)ave projects
- (D)Display projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
DEFAULT_FILE = "projects.txt"


def main():
    """..."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILE)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = get_valid_filename()
            projects = load_projects(DEFAULT_FILE)
            print(f"Loaded {len(projects)} from {filename}")
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
        choice = input(">>> ").upper()


def load_projects(file):
    """..."""
    with open(file, "r") as in_file:
        in_file.readline()
        projects = []
        for line in in_file:
            project = line.strip().split("\t")
            projects.append(Project(project[0], project[1], int(project[2]), float(project[3]), int(project[4])))
        return projects


def get_valid_filename():
    """..."""
    is_valid = False
    while not is_valid:
        try:
            filename = input("Filename: ")
            in_file = open(filename, "r")
            in_file.close()
            is_valid = True
        except FileNotFoundError:
            print("File does not exist in directory.")
    return filename


main()
