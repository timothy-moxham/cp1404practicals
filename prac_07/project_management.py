"""

Estimate: 60 minutes
Actual:
"""

from datetime import datetime
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
            filter_projects_by_date(projects)
        elif choice == "A":
            print("Let's add a new project")
            projects = add_new_project(projects)
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
        print(MENU)
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
            projects.append(
                Project(project[0], datetime.strptime(project[1], "%d/%m/%Y").date(), int(project[2]),
                        float(project[3]), int(project[4])))
        return projects


def save_projects(file, projects):
    """..."""
    with open(file, "w") as out_file:
        print("Name	Start Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


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


def filter_projects_by_date(projects):
    """..."""
    filter_date = get_valid_date()
    filtered_projects = sorted([project for project in projects if project.start_date >= filter_date])

    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """..."""
    name = get_valid_name()
    start_date = get_valid_date()
    priority = get_valid_number("Priority: ", 1, 9)
    cost_estimate = get_valid_number("Cost estimate: $", 0, 1000000)
    completion_percentage = get_valid_number("Percentage complete: ", 0, 100)
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def get_valid_number(prompt, minimum, maximum):
    """..."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(prompt))
            while not (maximum >= number >= minimum):
                print(f"Number must be between {minimum} and {maximum}")
                number = int(input(prompt))
            is_valid_number = True
            return number
        except ValueError:
            print("Input must be an integer")
    return number


def get_valid_name():
    name = input("Name: ")
    while name == "":
        print("Name cannot be blank")
        name = input("Name: ")
    return name


def get_valid_date():
    """..."""
    is_valid_date = False
    while not is_valid_date:
        try:
            date_string = input("Start date (dd/mm/yyyy): ")
            date = datetime.strptime(date_string, "%d/%m/%Y").date()
            while date > date.today():
                print("")
            is_valid_date = True
        except ValueError:
            print("Incorrect date format.")
    return date


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
