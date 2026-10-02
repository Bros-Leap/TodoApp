from datetime import datetime
import json
class todoList:
    def __init__(self):
        self.tasks = []
        self.filename = "task.json"
        #self.load_task()
    def adding_task(self,description):
        task = {
          'id': len(self.tasks) + 1,
          'description': description,
          'completed': False,
          'created_at': datetime.now().strftime("%Y-%M-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_task()
        print(f"Task {description} added successful.")
    
    def view_task(self):
        if not self.tasks:
            print("Task not Found!")
            return
        print("===> Your Task <===")
        print("-" * 50)
        for task in self.tasks:
            status = "Done" if task['completed'] else ""
            print(f"{task['id']}. [{status}] {task['description']}")
        print("-" * 50)
    def complete_task(self,task_id):
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


"""def main():
    print("Testing")"""

if __name__ == "__main__":
    todo = todoList()
    todo.adding_task("Hello world")
    todo.complete_task(1)
    todo.view_task()
    
    #main()