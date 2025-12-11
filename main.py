from todo_list import TodoList

def main():
    todo = TodoList()
    
    # Pruebas básicas
    print("=== To-Do List Manager ===")
    
    # Agregar tareas
    todo.add_task("Buy groceries", priority="high")
    todo.add_task("Pay bills", priority="medium")
    
    # Listar tareas
    print("\nTasks:")
    for task in todo.list_tasks():
        print(f"- {task.description} [{task.status}] - Priority: {task.priority}")
    
    # Marcar como completada
    todo.mark_completed("Buy groceries")
    
    print("\nAfter marking 'Buy groceries' as completed:")
    for task in todo.list_tasks():
        print(f"- {task.description} [{task.status}]")

if __name__ == "__main__":
    main()