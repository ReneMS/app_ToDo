"""
Componente de formulario de tarea.
"""

import reflex as rx
from todo_app.states.estado import Estado


def crear():
    Estado.crear_tarea()


def TaskForm() -> rx.Component:
    """Formulario para crear una nueva tarea."""
    return rx.box(
        rx.vstack(
            rx.heading("Nueva Tarea", size="5"),
            rx.input(
                placeholder="Título de la tarea",
                value=Estado.titulo,
                on_change=Estado.set_titulo,
                class_name="w-full px-3 py-2 border border-gray-300 rounded-lg",
            ),
            rx.text_area(
                placeholder="Descripción (opcional)",
                value=Estado.descripcion,
                on_change=Estado.set_descripcion,
                class_name="w-full px-3 py-2 border border-gray-300 rounded-lg",
                rows="3",
            ),
            rx.select(
                ["baja", "media", "alta"],
                value=Estado.prioridad,
                on_change=Estado.set_prioridad,
                placeholder="Prioridad",
            ),
            rx.cond(
                Estado.mensaje_error != "",
                rx.text(Estado.mensaje_error, color="red", size="2"),
            ),
            rx.button(
                "Crear Tarea",
                on_click=crear,
                class_name="bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 w-full",
            ),
            spacing="4",
        ),
        class_name="p-6 bg-white rounded-lg border border-gray-200 shadow-sm",
    )
