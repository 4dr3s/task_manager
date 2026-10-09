from task_manager import TaskManager

def main():
    print("\n--- Gestor de Tareas Inteligente ---")
    print("1. Añadir Tarea")
    print("2. Listar Tareas")
    print("3. Completar Tarea")
    print("4. Eliminar Tarea")
    print("5. Salir")
    task_manager = TaskManager()
    opcion = 0
    while(opcion != 5):
        try:
            opcion = int(input("Ingrese una opción: "))
            match(opcion):
                case 1:
                    add_task(task_manager)
                case 2:
                    task_manager.list_tasks()
                case 3:
                    complete_task(task_manager)
                case 4:
                    delete_task(task_manager)
                case 5:
                    print("--- Programa Terminado ---")
                case _:
                    print("Opción no válida")
        except ValueError:
            print(f"Error inesperado, opción no valida")
    
def add_task(task_manager: TaskManager):
    description = input("Ingrese la descripción de la Tarea: ")
    task_manager.add_task(description=description)

def complete_task(task_manager: TaskManager):
    id = int(input("Ingrese el id de la tarea a completar: "))
    task_manager.completa_task(id)

def delete_task(task_manager: TaskManager):
    id = int(input("Ingrese el id de la tarea a eliminar: "))
    task_manager.completa_task(id)

if __name__ == "__main__":
    main()