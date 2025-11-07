"""

Estimate: 60 minutes
Actual:
"""

import datetime
from project import Project

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
DEFAULT_FILE = "projects.txt"


def main():
    """..."""
    print("Welcome to Pythonic Project Management")
    filename = DEFAULT_FILE
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = get_valid_filename()
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            save_filename = input("Filename: ")
            save_projects(save_filename, projects)
            print(f"Saved {len(projects)} projects to {save_filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
        choice = input(">>> ").upper()

    choice = input(f"Would you like to save to {filename}? ").upper()
    if choice == "Y":
        save_projects(filename, projects)
        print(f"Saved {len(projects)} projects to {filename}")
    print("Thank you for using custom-built project management software.")


def load_projects(file):
    """..."""
    with open(file, "r") as in_file:
        in_file.readline()
        projects = []
        for line in in_file:
            project = line.strip().split("\t")
            projects.append(Project(project[0], project[1], int(project[2]), float(project[3]), int(project[4])))
        return projects


def save_projects(file, projects):
    """..."""
    with open(file, "w") as out_file:
        print("Name	Start Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                  f"{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """..."""
    incomplete_projects = sorted([project for project in projects if project.completion_percentage != 100])
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(" ", project)

    completed_projects = sorted([project for project in projects if project.completion_percentage == 100])
    print("Completed projects:")
    for project in completed_projects:
        print(" ", project)


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
