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



