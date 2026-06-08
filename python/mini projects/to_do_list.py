import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(BASE_DIR, "files", "task.json")

os.makedirs(os.path.dirname(file_name), exist_ok=True)

def load_task():
    try:
       with open (file_name,'r') as file:
           return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_task():
    with open(file_name,'w') as file:
        json.dump(to_do_list,file,indent=4)


to_do_list = load_task()
if not to_do_list:
    to_do_list = ["morning walk", "drink juice"]


# Add Task
def add_task():
    task = input("Enter a new task: ").strip().lower()

    if not task:
        print("❌ Task cannot be empty.")
        return

    if task in to_do_list:
        print(f"❌ '{task}' already exists.")
    else:
        to_do_list.append(task)
        print(f"✅ '{task}' added successfully!")


# Remove Task
def remove_task():
    if not to_do_list:
        print("📌 No tasks remaining.")
        return

    remaining_tasks()

    try:
        task_no = int(input("Enter task number to complete: "))

        if task_no < 1 or task_no > len(to_do_list):
            print("❌ Task number does not exist.")
            return

        removed_task = to_do_list.pop(task_no - 1)
        print(f"✅ '{removed_task}' completed successfully!")
    except ValueError:
        print("❌ Please enter a valid number.")


# Show Remaining Tasks
def remaining_tasks():
    if not to_do_list:
        print("📌 No tasks remaining.")
        return

    print("\n📋 Remaining Tasks:")
    for i, task in enumerate(to_do_list, start=1):
        print(f"{i}. {task}")


# Find Task
def find_task():
    task = input("Enter task to search: ").strip().lower()

    if task in to_do_list:
        print(f"🔍 '{task}' is still pending.")
    else:
        print(f"❌ '{task}' not found.")


# Menu
def menu():
    print("\n====================")
    print("      TO-DO LIST")
    print("====================")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Show Remaining Tasks")
    print("4. Find Task")
    print("0. Exit")


# Main Program
while True:
    menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    match choice:
        case 1:
            add_task()

        case 2:
            remove_task()

        case 3:
            remaining_tasks()

        case 4:
            find_task()

        case 0:
            save_task()
            print("👋 Goodbye!")
            break

        case _:
            print("❌ Invalid choice. Please select between 0 and 4.")