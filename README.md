# ToDo App - Sistema de Gestión de Tareas

Una aplicación web moderna para gestionar tareas personales, construida con **Reflex** (framework web en Python puro), **PostgreSQL** y **Tailwind CSS**.

## Características

- ✅ Autenticación de usuarios (registro e inicio de sesión)
- ✅ CRUD completo de tareas (crear, leer, actualizar, eliminar)
- ✅ Sistema de prioridades (baja, media, alta)
- ✅ Filtrado de tareas (todas, pendientes, completadas)
- ✅ Interfaz moderna con Tailwind CSS
- ✅ Base de datos PostgreSQL
- ✅ Diseño responsivo

## Tecnologías

- **Backend**: Python 3.12 + Reflex 0.8.28
- **Frontend**: React + Tailwind CSS
- **Base de datos**: PostgreSQL + SQLModel + Alembic
- **Autenticación**: bcrypt para hashing de contraseñas
- **Contenedores**: Docker + Docker Compose

## Requisitos

- Python 3.12+
- Docker y Docker Compose
- uv (gestor de paquetes)

## Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd todo_app
```

### 2. Configurar variables de entorno

Copia el archivo `.env.example` a `.env`:

```bash
cp .env.example .env
```

### 3. Iniciar PostgreSQL con Docker

```bash
docker-compose up -d postgres
```

### 4. Instalar dependencias

```bash
uv sync
```

### 5. Inicializar base de datos

```bash
uv run reflex db init
uv run reflex db migrate
```

### 6. Ejecutar la aplicación

```bash
uv run reflex run
```

La aplicación estará disponible en:
- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:8000

## Uso

1. Abre http://localhost:3000 en tu navegador
2. Regístrate con un nuevo usuario
3. Inicia sesión
4. Crea, edita y elimina tareas
5. Filtra tareas por estado

## Estructura del Proyecto

```
todo_app/
├── todo_app/
│   ├── models/           # Modelos de base de datos
│   │   ├── usuario.py   # Modelo de usuario
│   │   └── tarea.py     # Modelo de tarea
│   ├── states/          # Estados de la aplicación
│   │   └── estado.py    # Estado principal
│   ├── pages/           # Páginas de la aplicación
│   │   ├── auth.py      # Login y registro
│   │   └── dashboard.py # Dashboard de tareas
│   └── app.py          # Configuración principal
├── alembic/             # Migraciones de base de datos
├── docker-compose.yml   # Configuración de Docker
├── Dockerfile           # Imagen de producción
├── Dockerfile.dev       # Imagen de desarrollo
├── pyproject.toml       # Dependencias del proyecto
└── README.md           # Este archivo

```

## Comandos Docker

### Iniciar solo PostgreSQL
```bash
docker-compose up -d postgres
```

### Iniciar toda la aplicación
```bash
docker-compose up -d
```

### Ver logs
```bash
docker-compose logs -f
```

### Detener contenedores
```bash
docker-compose down
```

## Variables de Entorno

| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| DATABASE_URL | URL de conexión a PostgreSQL | postgresql://todo_user:todo_password@localhost:5432/todo_db |
| POSTGRES_HOST | Host de PostgreSQL | localhost |
| POSTGRES_PORT | Puerto de PostgreSQL | 5432 |
| POSTGRES_DB | Nombre de la base de datos | todo_db |
| POSTGRES_USER | Usuario de PostgreSQL | todo_user |
| POSTGRES_PASSWORD | Contraseña de PostgreSQL | todo_password |

## Desarrollo

### Estándares de código

- Sigue las convenciones de Python (PEP 8)
- Usa type hints para mejor mantenibilidad
- Los estados deben heredar de `rx.State`
- Para condicionales en templates usa `rx.cond` en lugar de `if`

### comandos útiles

```bash
# Recompilar después de cambios
uv run reflex run --frontend-only

# Regenerar migraciones
uv run reflex db makemigrations
uv run reflex db migrate
```

## Licencia

MIT License
