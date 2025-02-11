import sys

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file. If the file does not exist, return an empty list."""
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = f.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Save the current list of tasks to the file."""
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def list_tasks(tasks):
    """Print all tasks in the list."""
    if not tasks:
        print("No tasks!")
    else:
        for idx, task in enumerate(tasks):
            # Display tasks numbered starting at 1
            print(f"{idx + 1}. {task}")

def add_task(tasks, task):
    """Add a new task to the list and save."""
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

def remove_task(tasks, task_number):
    """
    Remove a task by its number and save.
    
    BUG: The user sees task numbers starting at 1, but this code removes using a 0-index,
         so it will remove the wrong task.
    """
    try:
        # Convert the provided task_number into an integer
        task_number = int(task_number)
        # BUG: This pops the task at index 'task_number', but should be 'task_number - 1'
        removed = tasks.pop(task_number)
        save_tasks(tasks)
        print(f"Task removed: {removed}")
    except IndexError:
        print("Invalid task number!")
    except ValueError:
        print("Task number must be an integer!")

def main():
    tasks = load_tasks()
    
    if len(sys.argv) < 2:
        print("Usage: python todo.py [list|add|remove] [task/task_number]")
        return

    command = sys.argv[1]
    
    if command == "list":
        list_tasks(tasks)
    
    elif command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task to add.")
            return
        # BUG: If the task contains multiple words, only the second argument is used.
        task = sys.argv[2]
        add_task(tasks, task)
    
    elif command == "remove":
        if len(sys.argv) < 3:
            print("Please provide a task number to remove.")
            return
        remove_task(tasks, sys.argv[2])
    
    else:
        print("Unknown command. Please use list, add, or remove.")

if __name__ == "__main__":
    main()
