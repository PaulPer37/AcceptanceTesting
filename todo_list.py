import sys

class Task:
    def __init__(self, name, priority="Media", category="General"):
        # Cumpliendo el requisito de mínimo 4 atributos 
        self.name = name
        self.status = "Pending"
        self.priority = priority
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
            if task.name == name:
                task.mark_completed()
                return f"Tarea '{name}' marcada como completada."
        return f"Tarea '{name}' no encontrada."

    def clear_list(self):
        # Funcionalidad sugerida 4: Limpiar lista [cite: 175]
        self.tasks = []
        return "Lista limpiada."

    def delete_task(self, name):
        # --- FUNCIONALIDAD EXTRA  ---
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.name != name]
        if len(self.tasks) < initial_count:
            return f"Tarea '{name}' eliminada."
        return f"Tarea '{name}' no encontrada."

    def get_task(self, name):
        # Helper para verificar estado en los tests
        for task in self.tasks:
            if task.name == name:
                return task
        return None

# Bloque para ejecución manual si se desea probar sin Behave
if __name__ == "__main__":
    todo = ToDoList()
    print("--- To-Do List Manager ---")
    todo.add_task("Comprar leche")
    print(todo.list_tasks())