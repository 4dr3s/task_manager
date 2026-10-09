import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from task_manager import Task, TaskManager


class TestTask(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.original_filename = TaskManager.FILENAME
        self.task_file = Path(self.tmp_dir.name) / "task.json"
        TaskManager.FILENAME = str(self.task_file)

    def tearDown(self):
        TaskManager.FILENAME = self.original_filename
        self.tmp_dir.cleanup()

    def test_task_string_representation(self):
        incomplete = Task(1, "Estudiar Python")
        complete = Task(2, "Enviar correo", completed=True)

        self.assertEqual(str(incomplete), "[ ] #1: Estudiar Python")
        self.assertEqual(str(complete), "[ok] #2: Enviar correo")

    def test_add_task_persists_task_and_advances_id(self):
        manager = TaskManager()

        manager.add_task("Preparar reunión")

        self.assertEqual(len(manager._tasks), 1)
        self.assertEqual(manager._tasks[0].id, 1)
        self.assertEqual(manager._tasks[0].description, "Preparar reunión")
        self.assertFalse(manager._tasks[0].completed)
        self.assertEqual(manager._next_id, 2)

        with self.task_file.open("r", encoding="utf-8") as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data, [{"id": 1, "description": "Preparar reunión", "completed": False}])

    def test_completa_task_marks_task_as_done(self):
        manager = TaskManager()
        manager._tasks = [Task(1, "Leer documentación"), Task(2, "Subir cambios")]
        manager._next_id = 3

        manager.completa_task(2)

        self.assertTrue(manager._tasks[1].completed)

        with self.task_file.open("r", encoding="utf-8") as file:
            saved_data = json.load(file)
        self.assertTrue(saved_data[1]["completed"])

    def test_delete_task_removes_task(self):
        manager = TaskManager()
        manager._tasks = [Task(1, "Tarea uno"), Task(2, "Tarea dos")]
        manager._next_id = 3

        manager.delete_task(1)

        self.assertEqual(len(manager._tasks), 1)
        self.assertEqual(manager._tasks[0].id, 2)
        self.assertEqual(manager._tasks[0].description, "Tarea dos")

        with self.task_file.open("r", encoding="utf-8") as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data, [{"id": 2, "description": "Tarea dos", "completed": False}])

    def test_load_task_reads_existing_json(self):
        payload = [
            {"id": 1, "description": "Primera tarea", "completed": False},
            {"id": 3, "description": "Tercera tarea", "completed": True},
        ]
        with self.task_file.open("w", encoding="utf-8") as file:
            json.dump(payload, file)

        manager = TaskManager()

        self.assertEqual(len(manager._tasks), 2)
        self.assertEqual(manager._tasks[0].description, "Primera tarea")
        self.assertEqual(manager._tasks[1].id, 3)
        self.assertEqual(manager._tasks[1].completed, True)
        self.assertEqual(manager._next_id, 4)

    def test_list_tasks_prints_empty_and_non_empty_lists(self):
        manager = TaskManager()
        buffer = io.StringIO()

        with redirect_stdout(buffer):
            manager.list_tasks()
        self.assertEqual(buffer.getvalue(), "No hay Tareas registradas\n")

        manager._tasks = [Task(1, "Revisar PR")]
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            manager.list_tasks()
        self.assertIn("[ ] #1: Revisar PR", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
