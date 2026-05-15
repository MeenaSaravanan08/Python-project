import json
import os

def get_task_id():
    if not os.path.exists("data.json"):
        return 1
    with open("data.json", "r") as file:
        all_tasks = json.load(file)
    if not all_tasks:
        return 1
    else:
        return int(all_tasks[-1]["Task id"]) + 1

def create(input):
    task_id = get_task_id()
    data = {
        "Todo": input,
        "is_completed": False,
        "Task id": task_id
    }
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            all_tasks = json.load(file)
    else:
        all_tasks = []
    all_tasks.append(data)
    with open("data.json", "w") as file:
        json.dump(all_tasks, file, indent=4)
    print(f"Task added: {input} (ID: {task_id})")

def read():
    if not os.path.exists("data.json"):
        print("No tasks found")
        return
    with open("data.json", "r") as file:
        all_tasks = json.load(file)
    if not all_tasks:
        print("No tasks found")
        return
    print("\n📋 My Tasks:")
    for task in all_tasks:
        status = "✔ Done" if task["is_completed"] else "✘ Pending"
        print(f"ID: {task['Task id']} | {task['Todo']} | {status}")

def update(task_id):
    with open("data.json", "r") as file:
        all_tasks = json.load(file)
    found = False
    for task in all_tasks:
        if task["Task id"] == task_id:
            task["is_completed"] = True
            found = True
            print(f"Task {task_id} marked as completed!")
    if not found:
        print("Task id not found")
        return
    with open("data.json", "w") as file:
        json.dump(all_tasks, file, indent=4)

def delete(task_id):
    with open("data.json", "r") as file:
        all_tasks = json.load(file)
    new_list = [task for task in all_tasks if task["Task id"] != task_id]
    if len(new_list) == len(all_tasks):
        print("Task id not found")
        return
    with open("data.json", "w") as file:
        json.dump(new_list, file, indent=4)
    print(f"Task {task_id} deleted")

def menu():
    while True:
        print("\n===== TO-DO MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task_name = input("Enter task name: ")
            create(task_name)
        elif choice == "2":
            read()
        elif choice == "3":
            task_id = int(input("Enter Task id: "))
            update(task_id)
        elif choice == "4":
            task_id = int(input("Enter Task id: "))
            delete(task_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

menu()

