from datetime import datetime
import json
class todoList:
    def __init__(self):
        self.tasks = []
        self.filename = "task.json"
    
    def adding_task(self,description):
        task = {
          'id': len(self.tasks) + 1,
          'description': description,
          'completed': False,
          'created_at': datetime.now().strftime("%Y-%M-%d %H:%M:%S")
        }
        self.tasks.append(task)
        print(f"Task {description} added successful.")

"""def main():
    print("Testing")"""

if __name__ == "__main__":
    todo = todoList()
    todo.adding_task("Hello world")
    #main()