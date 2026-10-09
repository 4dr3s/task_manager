# Task Manager

Aplicación de gestión de tareas en Python con interfaz de consola y soporte opcional para IA para descomponer tareas complejas en subtareas.

## Descripción

Task Manager es un gestor de tareas personal, pensado para registrar actividades, marcarlas como completadas y eliminarlas cuando ya no sean necesarias. El proyecto combina una lógica simple de almacenamiento en JSON con una integración opcional con OpenAI para ayudar a dividir tareas complejas en pasos más pequeños y accionables.

## Características

- Registro de tareas con identificador único
- Visualización de tareas pendientes y completadas
- Marcado de tareas como terminadas
- Eliminación de tareas
- Persistencia automática en un archivo `task.json`
- Integración con OpenAI para ayudar en la descomposición de tareas complejas
- Interfaz CLI interactiva en consola

## Requisitos

- Python 3.10 o superior
- pip
- Cuenta de OpenAI con una API key (solo si se quiere usar la función de IA)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/4dr3s/task_manager.git
   cd task_manager
   ```

2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura la variable de entorno para OpenAI:

   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

   ```env
   OPENAI_API_KEY=tu_api_key_aqui
   ```

   Si no defines esta variable, la funcionalidad de IA se deshabilitará con un mensaje de error.

## Ejecución

Ejecuta la aplicación desde la raíz del proyecto:

```bash
python main.py
```

Se mostrará un menú con las siguientes opciones:

1. Añadir tarea
2. Añadir tarea compleja (con IA)
3. Listar tareas
4. Completar tarea
5. Eliminar tarea
6. Salir

## Uso

### 1. Agregar una tarea simple

Selecciona la opción `1` y escribe la descripción de la tarea.

### 2. Agregar una tarea compleja con IA

Selecciona la opción `2` e ingresa una descripción detallada.

La función `create_simple_task()` intenta dividir la tarea en varias subtareas usando el modelo de OpenAI configurado. La respuesta esperada es una lista de subtareas en formato de viñetas.

### 3. Ver tareas

Selecciona la opción `3` para listar todas las tareas registradas junto con su estado.

### 4. Completar tarea

Elige la opción `4` e indica el ID de la tarea a marcar como completada.

### 5. Eliminar tarea

Usa la opción `5` e indica el ID de la tarea a eliminar.

## Estructura del proyecto

```text
task_manager/
├── .env                     # Variables de entorno locales
├── .gitignore              # Archivos ignorados por Git
├── LICENSE                 # Licencia del proyecto
├── README.md               # Documentación del proyecto
├── ai_service.py           # Integración con OpenAI
├── main.py                 # Punto de entrada CLI
├── requirements.txt        # Dependencias del proyecto
├── task.json               # Archivo de persistencia de tareas
├── task_manager.py         # Lógica principal del gestor de tareas
├── tests/
│   └── test_task_manager.py
└── .venv                   # Entorno virtual (si se crea localmente)
```

## Persistencia

Las tareas se guardan en un archivo JSON llamado `task.json` en la raíz del proyecto. Cada tarea incluye:

- `id`: identificador único
- `description`: texto de la tarea
- `completed`: estado de finalización

## Dependencias principales

El proyecto usa estas bibliotecas:

- `openai`: cliente oficial para consumir la API de OpenAI
- `python-dotenv`: carga variables de entorno desde el archivo `.env`

Puedes ver la lista completa en [requirements.txt](requirements.txt).

## Pruebas

El proyecto incluye pruebas unitarias para validar el comportamiento del gestor de tareas.

Ejecuta:

```bash
python -m unittest discover -s tests
```

## Notas

- La aplicación está pensada como una herramienta de consola simple y didáctica.
- La integración con IA es opcional y depende de una API key válida.
- Si el archivo `task.json` no existe, la aplicación lo crea al guardar la primera tarea.

## Licencia

Este proyecto se distribuye bajo la licencia indicada en [LICENSE](LICENSE).
