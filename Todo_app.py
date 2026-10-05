from datetime import datetime
import json
class todoList:
    def __init__(self):
        self.tasks = []
        self.filename = "task.json"
        self.load_task()
    def adding_tasks(self,description):
        task = {
          'id': len(self.tasks) + 1,
          'description': description,
          'completed': False,
          'created_at': datetime.now().strftime("%Y-%M-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_task()
        print(f"Task {description} added successful.") 
    def view_tasks(self):
        if not self.tasks:
            print("Task not Found!")
            return
        print("===> Your Task <===")
        print("-" * 50)
        for task in self.tasks:
            status = "Done" if task['completed'] else ""
            print(f"{task['id']}. [{status}] {task['description']}")
        print("-" * 50)
    def completed_tasks(self,task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_task()
                print(f"Task with ID {task_id} mark as completed.")
                return
        print(f"Task with ID {task_id} not foound!")
    def delete_task(self,task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_task()
                print(f"Task with ID {task_id} deleted!")
                return
            print(f"Task with ID {task_id} not found!")
    def save_task(self):
        with open(self.filename,'w') as file:
            json.dump(self.tasks,file,indent=2)
    def load_task(self):
        try:
            with open(self.filename,'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.task = []


def main():
    todo = todoList()

    while True:
        print("===> Menu Task Application <===")
        print("1.Add Task.")   
        print("2.View Task.") 
        print("3.Complete Task.") 
        print("4.Delet Task.") 
        print("5.Exit.")

        choice = input("\nChoose your option(1-5):")   

        if choice == '1':
            description = input("Enter your Description:")
            todo.adding_tasks(description=description)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter ID of task that you want to completed:"))
                todo.completed_tasks(task_id = task_id)
            except ValueError:
                print("Please enter a valid ID!")
        elif choice == '4':
            try:
                todo.view_tasks()
                task_id = int(input("Enter ID of task that you want to deleted:"))
                todo.delete_task(task_id = task_id)
            except ValueError:
                print("Please enter a valid ID!")
        elif choice == '5':
            print("Thank you see you again!")
            break
        else:
            print("Invaid choice! Try again!")

if __name__ == "__main__":
    main()