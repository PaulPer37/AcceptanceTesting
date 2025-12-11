import sys

class Task:

    def __init__(self, description, priority="medium", due_date=None, category="general"):
        self.description = description
        self.status = "Pending"
        self.priority = priority
        self.due_date = due_date

        self.category = category

    def mark_completed(self):
        self.status = "Completed"

    def __str__(self):
        return f"{self.name} | Estado: {self.status} | Prio: {self.priority} | Cat: {self.category}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority="Media", category="General"):
        # Funcionalidad sugerida 1: Agregar tarea [cite: 172]
        task = Task(name, priority, category)
        self.tasks.append(task)
        return f"Tarea '{name}' agregada."

    def list_tasks(self):
        # Funcionalidad sugerida 2: Listar tareas [cite: 173]
        if not self.tasks:
            return "La lista está vacía."
        output = "Tasks:\n"
        for task in self.tasks:
            output += f"{task.name}\n" # Simplificado para coincidir con el escenario del PDF
        return output.strip()

    def mark_task_completed(self, name):
        # Funcionalidad sugerida 3: Marcar como completada [cite: 174]
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

