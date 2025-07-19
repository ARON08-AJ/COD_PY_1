tasks = []

def menu():
    print("TO-DO LIST MENU DRIVEN : ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("\nEnter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully.\n")
    
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "Completed" if t["completed"] else "Not Completed"
        print(f"{i}. {t['task']} [{status}]")
    print()

def mark_completed():
    if not tasks:
        print("No tasks to mark as completed.\n")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "Completed" if t["completed"] else "Not Completed"
        print(f"{i}. {t['task']} [{status}]")
    try:
        task_num = int(input("\nEnter task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as completed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task():
    if not tasks:
        print("No tasks to delete.\n")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "Completed" if t["completed"] else "Not Completed"
        print(f"{i}. {t['task']} [{status}]")
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Deleted task: {removed['task']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")
        
while True:
    menu()
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
