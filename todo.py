tasks = []

def add_task():
    """Adds a task to the to-do list."""
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    """Views all tasks in the to-do list."""
    if not tasks:
        print("No tasks to view.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    """Deletes a task from the to-do list."""
    view_tasks()
    if not tasks:
        return

    try:
        task_num_to_delete = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num_to_delete <= len(tasks):
            deleted_task = tasks.pop(task_num_to_delete - 1)
            print(f"Task '{deleted_task}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the to-do list application."""
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Thank you for using the To-Do List Application!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
