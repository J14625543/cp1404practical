import datetime
from operator import attrgetter
from prac_07.project import Project

def start_program():
    print("Pythonic Project Manager Ready!")
    project_list = read_projects("projects.txt")
    print(f"{len(project_list)} projects successfully loaded.")

    while True:
        show_options()
        choice = input("Your selection: ").strip().upper()

        if choice == "L":
            filename = input("Filename to load from: ")
            project_list = read_projects(filename)
            print(f"Reloaded {len(project_list)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename to save to: ")
            write_projects(project_list, filename)
            print(f"Projects saved to {filename}")
        elif choice == "D":
            show_project_list(project_list)
        elif choice == "F":
            show_filtered_projects(project_list)
        elif choice == "A":
            create_project(project_list)
        elif choice == "U":
            modify_project(project_list)
        elif choice == "Q":
            should_save = input("Save to projects.txt before quitting? (y/n): ").strip().lower()
            if should_save.startswith("y"):
                write_projects(project_list, "projects.txt")
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Please choose a valid option.")

def show_options():
    """Print available actions"""
    print("\nMenu:")
    print("L - Load project file")
    print("S - Save current projects")
    print("D - Display all projects")
    print("F - Filter projects by start date")
    print("A - Add a new project")
    print("U - Update existing project")
    print("Q - Quit")

def read_projects(filename):
    """Read projects from the specified file"""
    project_data = []
    try:
        with open(filename, "r") as file:
            file.readline()  # Skip header
            for line in file:
                items = line.strip().split("\t")
                if len(items) == 5:
                    project_data.append(Project(*items))
                else:
                    print(f"Warning: Line skipped due to format issue: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return project_data

def write_projects(projects, filename):
    """Write project data to a file"""
    with open(filename, "w") as file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=file)
        for p in projects:
            file.write(f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t{p.priority}\t"
                       f"{p.cost_estimate:.2f}\t{p.completion_percentage}\n")

def show_project_list(projects):
    """Display projects grouped by completion status"""
    print("\n--- Incomplete Projects ---")
    for p in sorted([x for x in projects if not x.completed()]):
        print(f"  {p}")

    print("--- Completed Projects ---")
    for p in sorted([x for x in projects if x.completed()]):
        print(f"  {p}")

def show_filtered_projects(projects):
    """Display projects starting after a user-specified date"""
    date_input = input("Enter cutoff date (dd/mm/yyyy): ")
    try:
        cutoff = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
        matching = [p for p in projects if p.start_date > cutoff]
        for proj in sorted(matching, key=attrgetter("start_date")):
            print(proj)
    except ValueError:
        print("Error: Invalid date. Use format dd/mm/yyyy.")







