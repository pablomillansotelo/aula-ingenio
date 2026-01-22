# Aula Ingenio

## Descripción General
Aula Ingenio es una plataforma educativa integral diseñada para la gestión de aulas, alumnos y procesos académicos. El objetivo del proyecto es facilitar la administración de cursos, inscripciones, actividades y calificaciones, proporcionando una herramienta centralizada tanto para administradores como para alumnos.

## Estructura del Proyecto
El repositorio está dividido en dos componentes principales:

### 1. aula-django
Contiene el código fuente de la aplicación web, construida con el framework **Django**. Esta carpeta incluye:
- **Backend**: Lógica de negocio, modelos de datos y API.
- **Frontend**: Plantillas HTML y archivos estáticos (CSS/JS) para la interfaz de usuario.
- **Apps**: Módulos separados para diferentes funcionalidades (`aula`, `alumnos`, `api`).

### 2. aula-sql
Contiene archivos relacionados con la base de datos:
- Scripts de inicialización SQL (`init.sql`).
- Diagramas de Entidad-Relación (`database.erd`) que describen el esquema de datos.

## Propósito de Negocio
El sistema busca resolver la necesidad de un control académico eficiente, permitiendo:
- **Gestión de Alumnos**: Registro y seguimiento de información personal y académica.
- **Cursos e Inscripciones**: Administración de la oferta académica y matriculación de estudiantes.
- **Evaluación**: Creación de actividades, tareas y exámenes, junto con su calificación.
- **Kardex**: Generación de reportes de calificaciones y promedios por alumno.

## Tecnologías Principales
- **Lenguaje**: Python 3
- **Framework Web**: Django 4.2
- **Base de Datos**: PostgreSQL (configuración recomendada) o SQLite (desarrollo).
- **Despliegue**: Configurado para ser compatible con Vercel.
