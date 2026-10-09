class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "ok" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"

class TaskManager:
    def __init__(self):
        self._tasks: list[Task] = []
        self._next_id: int = 1

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
        print(f"Tarea anadida: {description}")

    def completa_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Tarea completada: {task}")
                return
        print(f"Tarea no encontrada con id {id}")

    def delete_task(self, id):
        # for index, task in self._tasks:
        for task in self._tasks:
            if task.id == id:
                # self._tasks.pop(index)
                self._tasks.remove(task)
                print(f"Tarea co id {id} eliminada")
                return
        print(f"Tarea no encontrada con id {id}")