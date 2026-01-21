# Arquitectura del Proyecto

El proyecto sigue el patrón de diseño **MVT (Model-View-Template)** estándar de Django, organizado en múltiples aplicaciones ("apps") para separar responsabilidades.

## Estructura de Aplicaciones

### 1. `api` (Configuración)
No es una aplicación en el sentido funcional, sino el contenedor de la configuración global del proyecto.
- **settings.py**: Configuración de bases de datos, aplicaciones instaladas, middleware, etc.
- **urls.py**: Enrutador principal que despacha las peticiones a las apps correspondientes.
- **wsgi.py**: Punto de entrada para servidores web WSGI (como Gunicorn).

### 2. `aula` (Core)
Esta aplicación contiene el corazón de la lógica de negocio y los modelos de datos.
- **Responsabilidad**: Definir la estructura de la base de datos (Modelos) y gestionar la lógica administrativa.
- **Modelos**: Alumno, Curso, Inscripcion, Actividad, etc.
- **Vistas**: Dashboard principal (`/dashboard/`).

### 3. `alumnos` (Portal de Estudiante)
Aplicación dedicada a la interfaz y funcionalidades específicas para los estudiantes.
- **Responsabilidad**: Mostrar información relevante para el usuario final (alumno).
- **Vistas**:
    - Kardex
    - Horario
    - Pagos
    - Listado de alumnos (si aplica).

## Flujo de Datos
1. El usuario realiza una petición (ej. `/alumnos/kardex/`).
2. `api/urls.py` recibe la petición y la delega a `alumnos/urls.py`.
3. La vista en `alumnos/views.py` procesa la solicitud.
4. La vista consulta los modelos definidos en `aula/models.py` para obtener datos.
5. La vista renderiza una plantilla HTML (`templates/`) con los datos y la devuelve al usuario.

## Base de Datos
El proyecto está configurado para soportar múltiples bases de datos (Routing), aunque por defecto utiliza una configuración estándar.
- **Router de Autenticación**: Existe una configuración (`api.dbrouters.auth_router.AuthRouter`) preparada para separar las tablas de usuarios (`auth_user`, etc.) en una base de datos distinta si fuera necesario.

## Frontend
- El frontend se sirve a través de plantillas de Django (Django Templates).
- Los archivos estáticos (CSS, JS) se gestionan en las carpetas `static/`.
