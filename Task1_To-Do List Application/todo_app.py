import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add Task
def add_task(tasks):
    description = input("Task Description: ")
    priority = input("Priority (High/Medium/Low): ")
    due_date = input("Due Date (DD-MM-YYYY): ")

    task = {
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task Added Successfully!")

# View Tasks
def view_tasks(tasks):
    if not tasks:
        print("No Tasks Found.")
        return

    print("\n===== TASK LIST =====")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(
            f"{i}. {task['description']} | "
            f"Priority: {task['priority']} | "
            f"Due: {task['due_date']} | "
            f"{status}"
        )

# Complete Task
def complete_task(tasks):
    view_tasks(tasks)

    try:
        task_no = int(input("\nEnter Task Number: "))
        tasks[task_no - 1]["completed"] = True
        save_tasks(tasks)
        print("Task Marked as Completed!")
    except:
        print("Invalid Input!")

# Delete Task
def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_no = int(input("\nEnter Task Number to Delete: "))
        deleted = tasks.pop(task_no - 1)
        save_tasks(tasks)

        print(f"{deleted['description']} Deleted.")
    except:
        print("Invalid Input!")

# Search Task
def search_task(tasks):
    keyword = input("Enter Keyword: ").lower()

    found = False

    for task in tasks:
        if keyword in task["description"].lower():
            print(task)
            found = True

    if not found:
        print("Task Not Found.")

# Sort Tasks
def sort_priority(tasks):

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    tasks.sort(
        key=lambda x: priority_order.get(
            x["priority"],
            4
        )
    )

    print("Tasks Sorted by Priority.")
    view_tasks(tasks)

# Statistics
def show_statistics(tasks):

    total = len(tasks)

    completed = sum(
        1 for task in tasks
        if task["completed"]
    )

    pending = total - completed

    print("\n===== TASK STATISTICS =====")
    print(f"Total Tasks      : {total}")
    print(f"Completed Tasks  : {completed}")
    print(f"Pending Tasks    : {pending}")

# Theme
def change_theme():

    print("\nTheme Settings")
    print("1. Light Theme")
    print("2. Dark Theme")

    choice = input("Select Theme: ")

    if choice == "1":
        print("Light Theme Selected")
    elif choice == "2":
        print("Dark Theme Selected")
    else:
        print("Invalid Choice")

# Main Menu
def main():

    tasks = load_tasks()

    while True:

        print("\n============================")
        print(" SMART TO-DO LIST SYSTEM ")
        print("============================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Sort by Priority")
        print("7. Statistics")
        print("8. Theme Settings")
        print("9. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            search_task(tasks)

        elif choice == "6":
            sort_priority(tasks)

        elif choice == "7":
            show_statistics(tasks)

        elif choice == "8":
            change_theme()

        elif choice == "9":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()