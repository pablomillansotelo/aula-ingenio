# Guía de Instalación y Configuración

Esta guía detalla los pasos para levantar el entorno de desarrollo localmente.

## Requisitos del Sistema
- **Sistema Operativo**: Windows, macOS o Linux.
- **Python**: Versión 3.9 o superior.
- **Base de Datos**: PostgreSQL 12+ (Recomendado) o SQLite (incluido con Python).

## Pasos de Instalación

### 1. Clonar el Repositorio
```bash
git clone <url-del-repositorio>
cd aula-django
```

### 2. Entorno Virtual
Es crucial usar un entorno virtual para aislar las dependencias del proyecto.

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Variables de Entorno
El proyecto utiliza `python-decouple` para gestionar la configuración sensible. Debes crear un archivo llamado `.env` en la raíz de `aula-django`.

**Ejemplo de archivo `.env`:**

```ini
# --- Configuración Django ---
# Clave secreta para firma criptográfica. En producción usa una cadena larga y aleatoria.
SECRET_KEY=django-insecure-tu-clave-secreta-aqui
# Modo Debug. True para desarrollo, False para producción.
DEBUG=True

# --- Base de Datos (PostgreSQL) ---
# Si no se definen, se usará SQLite por defecto.
DB_NAME=aula_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

# --- Base de Datos de Autenticación (Auth) ---
# Django permite usar múltiples bases de datos. Esta configuración es para una DB de usuarios separada si se requiere.
AUTH_NAME=auth_db
AUTH_USER=postgres
AUTH_PASSWORD=postgres
AUTH_HOST=localhost
AUTH_PORT=5432
```

### 5. Base de Datos
Si usas PostgreSQL, asegúrate de crear las bases de datos definidas en el `.env` antes de continuar (`aula_db` y `auth_db` en el ejemplo anterior).

```sql
CREATE DATABASE aula_db;
CREATE DATABASE auth_db;
```

### 6. Migraciones
Aplica los cambios en la estructura de base de datos definidos por los modelos de Django.

```bash
python manage.py migrate
```

### 7. Superusuario (Opcional)
Para acceder al panel de administración de Django (`/admin/`):

```bash
python manage.py createsuperuser
```

### 8. Ejecutar Servidor
```bash
python manage.py runserver
```

Visita `http://127.0.0.1:8000/` en tu navegador.
