# Aula Django

## Descripción Técnica
Este directorio contiene la aplicación web desarrollada en **Django 4.2**. La aplicación sirve como el núcleo del sistema Aula Ingenio, manejando la lógica de negocio, la interacción con la base de datos y la presentación de la interfaz de usuario.

## Requisitos Previos
- Python 3.9 o superior.
- pip (gestor de paquetes de Python).
- Virtualenv (recomendado).
- PostgreSQL (opcional, por defecto usa SQLite si no se configura Postgres).

## Configuración e Instalación

1. **Clonar el repositorio y navegar a la carpeta:**
   ```bash
   cd aula-django
   ```

2. **Crear un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**
   Crea un archivo `.env` en la raíz de `aula-django` (donde está `manage.py`) con las siguientes variables. Se usa `python-decouple` para leerlas.

   ```env
   # Configuración General
   SECRET_KEY=tu_clave_secreta_aqui
   DEBUG=True

   # Base de Datos Principal (PostgreSQL)
   DB_NAME=nombre_db
   DB_USER=usuario_db
   DB_PASSWORD=password_db
   DB_HOST=localhost
   DB_PORT=5432

   # Base de Datos de Autenticación (Opcional, si se usa una separada)
   AUTH_NAME=auth_db
   AUTH_USER=auth_user
   AUTH_PASSWORD=auth_password
   AUTH_HOST=localhost
   AUTH_PORT=5432
   ```
   > Nota: Si no se configuran las variables de base de datos, Django intentará usar SQLite por defecto para la base `default`.

5. **Aplicar migraciones:**
   ```bash
   python manage.py migrate
   ```

6. **Ejecutar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```
   El servidor estará disponible en `http://127.0.0.1:8000/`.

## Estructura del Proyecto

- **api/**: Contiene la configuración principal del proyecto Django (`settings.py`, `urls.py`, `wsgi.py`). Aquí se definen las aplicaciones instaladas, bases de datos y rutas raíz.
- **aula/**: Aplicación principal ("Core") que contiene los modelos de negocio (`Alumno`, `Curso`, `Actividad`, etc.) y la lógica del dashboard principal.
- **alumnos/**: Aplicación enfocada en las funcionalidades para el estudiante (vista de calificaciones, horario, etc.).
- **templates/**: Plantillas HTML globales.
- **static/** y **staticfiles/**: Archivos estáticos (CSS, JS, imágenes).
- **manage.py**: Utilidad de línea de comandos de Django para tareas administrativas.

## Documentación Adicional
Para más detalles sobre la arquitectura y modelos, consulta la carpeta `docs/`.
