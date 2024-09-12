# Mi Proyecto Flask

## Descripción

Este es un proyecto de ejemplo utilizando Flask para construir una aplicación web. La estructura del proyecto está organizada para facilitar la modularidad y el mantenimiento. La aplicación incluye una configuración básica, modelos, rutas, y una estructura de directorios para manejar archivos estáticos, plantillas, y esquemas de datos.

## Estructura del Proyecto

```
mi_proyecto/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   └── users.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── public.py
│   │   └── users.py
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   │   ├── public/
│   │   ├── users/
│   │   └── private/
│   ├── schemas/
│   │   └── users.py
│   └── config.py
├── migrations/
│   └── ... (archivos de migración)
├── tests/
│   ├── __init__.py
│   ├── test_basic.py
│   └── test_models.py
├── run.py
└── requirements.txt
└── README.md
```

## Instalación

1. **Clonar el Repositorio**

   ```bash
   git clone <URL-del-repositorio>
   cd mi_proyecto
   ```

2. **Crear un Entorno Virtual**

   ```bash
   python3 -m venv venv
   ```

3. **Activar el Entorno Virtual**

   ```bash
   # En macOS/Linux
   source venv/bin/activate
   
   # En Windows
   venv\Scripts\activate
   ```

4. **Instalar las Dependencias**

   ```bash
   pip install -r requirements.txt
   ```

## Configuración

1. **Configurar la Base de Datos**

   Asegúrate de actualizar el archivo `config.py` con la URI de tu base de datos MySQL:

   ```python
   SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://user:password@localhost/db_name'
   ```

2. **Realizar Migraciones**

   Inicializa la base de datos y aplica las migraciones:

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

## Ejecución de la Aplicación

1. **Ejecutar la Aplicación**

   Asegúrate de estar en el entorno virtual y luego ejecuta:

   ```bash
   python run.py
   ```

   La aplicación debería estar disponible en `http://127.0.0.1:5000`.

## Pruebas

1. **Ejecutar Pruebas**

   Puedes ejecutar las pruebas definidas en la carpeta `tests` con:

   ```bash
   pytest
   ```

## Documentación

- **Rutas RESTful**: Los endpoints están definidos en `app/routes/`.
- **Modelos de Datos**: Los modelos están definidos en `app/modules/`.
- **Esquemas de Serialización**: Los esquemas de Marshmallow están en `app/schemas/`.

