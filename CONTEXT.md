# Contexto del Proyecto: Sistema ToDo con Reflex

## Objetivo
Crear un sistema de tareas (ToDo) completo con:
- Framework: **Reflex** (v0.8.28)
- Lenguaje: **Python** 3.12+
- Gestor: **uv**
- Base de datos: **PostgreSQL** (Docker)
- UI: **Tailwind CSS**
- Autenticación: Implementación propia con bcrypt

## Estado del Proyecto

### Completado ✅
- Proyecto inicializado con uv
- Modelos SQLModel (Usuario, Tarea)
- Estado único con autenticación y CRUD
- Landing Page profesional
- Página de Login/Registro con diseño moderno
- Base de datos inicializada con migraciones
- Usuario de prueba creado (demo / demo123)
- README.md documentación

### Pendiente
- Subir a GitHub

## Estructura
```
todo_app/
├── todo_app/
│   ├── models/          # usuario.py, tarea.py
│   ├── states/         # estado.py (principal)
│   ├── pages/          # auth.py, dashboard.py
│   └── app.py          # Landing Page + rutas
├── docker-compose.yml
├── alembic/            # Migraciones
├── crear_demo.py       # Script usuario prueba
└── README.md
```

## Notas Técnicas IMPORTANTES

### Reflex 0.8.x - Reglas de sintaxis:
1. **NO usar strings para tamaños** - Usar numeros: `size="3"` (no `size="lg"`)
2. **NO usar "start" en align** - Usar: "left", "center", "right"
3. **NO usar spacing > 9** - Maximo: "9"
4. **Auto setters deprecated** - Usar `auto_setters = True` en estados
5. **rx.cond para condicionales** - NO usar `if` en templates
6. **rx.Model para modelos** - NO SQLModel directo

### Para eventos on_click:
- Usar lambdas: `on_click=lambda: Estado.metodo(param)`
- Los metodos deben tener `self` como primer parametro

### Comandos:
```bash
# Iniciar app
cd todo_app && uv run reflex run

# PostgreSQL en Docker
docker-compose up -d postgres

# Crear usuario demo
uv run python crear_demo.py
```

### Credenciales de prueba:
- Usuario: **demo**
- Contraseña: **demo123**

## Errores Comunes y Soluciones

| Error | Solucion |
|-------|----------|
| `size="lg"` | Usar `size="3"` |
| `align="start"` | Usar `align="left"` |
| `spacing="16"` | Usar `spacing="9"` |
| `if` en template | Usar `rx.cond()` |
