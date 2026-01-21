# Modelos de Datos

El núcleo de la lógica de negocio reside en la aplicación `aula`. A continuación se describen los modelos principales definidos en `aula/models.py`.

## Diagrama Conceptual
Los modelos están relacionados para vincular alumnos con cursos y sus respectivas calificaciones.

`Alumno` <-> `Inscripcion` <-> `Curso` -> `Actividad` -> `CalificacionActividad`

## Descripción de Entidades

### Alumno
Representa a un estudiante en el sistema.
- **user**: Relación uno a uno con el modelo `User` de Django (autenticación).
- **nombre**: Nombre del alumno.
- **apellido**: Apellido del alumno.
- **curp**: Identificador único (Clave Única de Registro de Población).
- **email**: Correo electrónico único.
- **fecha_nacimiento**: Fecha de nacimiento.

### Curso
Representa una materia o asignatura impartida.
- **nombre**: Título del curso.
- **descripcion**: Detalles sobre el curso.
- **fecha_inicio / fecha_fin**: Periodo de duración.

### Inscripcion
Tabla intermedia que vincula a un `Alumno` con un `Curso`.
- **alumno**: Referencia al modelo Alumno.
- **curso**: Referencia al modelo Curso.
- **fecha_inscripcion**: Cuándo se inscribió.
- **intento**: Número de veces que ha cursado la materia (por defecto 1).

### Actividad
Tareas, exámenes o proyectos asignados dentro de un curso.
- **curso**: Curso al que pertenece la actividad.
- **nombre**: Título de la actividad.
- **valor**: Puntaje máximo (ej. 100).
- **tipo**: Categoría (Tarea, Examen, Proyecto, Participación).
- **estado**: Activa o Cerrada.

### CalificacionActividad
Registro de la calificación de un alumno en una actividad específica.
- **actividad**: Referencia a la actividad.
- **inscripcion**: Referencia a la inscripción del alumno (vincula alumno y curso).
- **calificacion**: Nota obtenida.
- **entregado**: Booleano que indica si se envió la tarea.

### Kardex
Resumen del desempeño de un alumno en un curso.
- **inscripcion**: Vinculación.
- **calificacion_final**: Promedio final calculado.
- **calcular_promedio()**: Método auxiliar para computar la nota final basada en las actividades.
