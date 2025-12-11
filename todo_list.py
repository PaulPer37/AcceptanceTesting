class Task:
    def __init__(self, description, priority="medium", due_date=None, category="general"):
        self.description = description
        self.status = "Pending"
        self.priority = priority
        self.due_date = due_date
        self.category = category

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description, priority="medium", due_date=None, category="general"):
        task = Task(description, priority, due_date, category)
        self.tasks.append(task)
        return task
    
    def list_tasks(self):
        return self.tasks
    
    def mark_completed(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.status = "Completed"
                return True
        return False
    
    def clear_all(self):
        self.tasks.clear()
    
    def is_empty(self):
        return len(self.tasks) == 0
    
    def delete_task(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                self.tasks.remove(task)
                return True
        return False