from task_manager import TaskManager
from ai_service import create_simple_task

def main():
    print("\n--- Gestor de Tareas Inteligente ---")
    print("1. Añadir Tarea")
    print("2. Añadir Tarea Compleja (con IA)")
    print("3. Listar Tareas")
    print("4. Completar Tarea")
    print("5. Eliminar Tarea")
    print("6. Salir")
    task_manager = TaskManager()
    opcion = 0
    while(opcion != 6):
        try:
            opcion = int(input("Ingrese una opción: "))
            match(opcion):
                case 1:
                    add_task(task_manager)
                case 2:
                    description = input("Descripción de la tarea compleja: ")
                    subtasks = create_simple_task(description)
                    for substask in subtasks:
                        if not substask.startswith("Error:"):
                            add_task_with_description(task_manager, description)
                        else:
                            print(substask)
                            break
                case 3:
                    task_manager.list_tasks()
                case 4:
                    complete_task(task_manager)
                case 5:
                    delete_task(task_manager)
                case 6:
                    print("--- Programa Terminado ---")
                case _:
                    print("Opción no válida")
        except ValueError:
            print(f"Error inesperado, opción no valida")
    
def add_task(task_manager: TaskManager):
    description = input("Ingrese la descripción de la Tarea: ")
    task_manager.add_task(description=description)

def add_task_with_description(task_manager: TaskManager, description):
    task_manager.add_task(description=description)

def complete_task(task_manager: TaskManager):
    id = int(input("Ingrese el id de la tarea a completar: "))
    task_manager.completa_task(id)

def delete_task(task_manager: TaskManager):
    id = int(input("Ingrese el id de la tarea a eliminar: "))
    task_manager.completa_task(id)

if __name__ == "__main__":
    main()