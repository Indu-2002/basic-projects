class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        print("To-Do List:")
        if not self.tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task['name']} - {'Completed' if task['completed'] else 'Pending'}")

    def add_task(self, task_name):
        self.tasks.append({'name': task_name, 'completed': False})
        print(f"Task '{task_name}' added to the to-do list.")

    def mark_task_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['name']}' removed from the to-do list.")
        else:
            print("Invalid task number.")

# Main application loop
def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application Menu:")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task_name = input("Enter the task name: ")
            todo_list.add_task(task_name)
        elif choice == '3':
            todo_list.display_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_completed(task_number)
        elif choice == '4':
            todo_list.display_tasks()
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
