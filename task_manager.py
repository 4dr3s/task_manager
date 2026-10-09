import json

class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "ok" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"

class TaskManager:
    FILENAME = "task.json"

    def __init__(self):
        self._tasks: list[Task] = []
        self._next_id: int = 1
        self.load_task()

    def list_tasks(self):
        """Listar Tareas"""
        if not self._tasks:
            print("No hay Tareas registradas")
        else:
            for task in self._tasks:
                print(task)

    def add_task(self, description):
        task = Task(self._next_id, description= description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Tarea añadida: {description}")
        self.save_tasks()

    def completa_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Tarea completada: {task}")
                self.save_tasks()
                return
        print(f"Tarea no encontrada con id {id}")

    def delete_task(self, id):
        # for index, task in self._tasks:
        for task in self._tasks:
            if task.id == id:
                # self._tasks.pop(index)
                self._tasks.remove(task)
                print(f"Tarea co id {id} eliminada")
                self.save_tasks()
                return
        print(f"Tarea no encontrada con id {id}")

    def load_task(self):
        try:
            with open(self.FILENAME, "r", encoding="utf-8",) as file:
                data = json.load(file)
                self._tasks = [Task(item["id"], item["description"], item["completed"]) for item in data]
                if self._tasks:
                    self._next_id = self._tasks[-1].id + 1
                else:
                    self._next_id = 1
        except FileNotFoundError:
            print("Archivo no encontrado")
        except Exception:
            print("Error no previsto")

    def save_tasks(self):
        try:
            with open(self.FILENAME, "w", encoding="utf-8") as file:
                json.dump([{"id": task.id, "description": task.description, "completed": task.completed} for task in self._tasks], file, indent=4)
        except PermissionError:
            print("No tiene permisos de escritura")