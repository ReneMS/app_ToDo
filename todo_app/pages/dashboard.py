"""
Página del dashboard de tareas - Versión simplificada.
"""

import reflex as rx
from todo_app.states.estado import Estado
from todo_app.models.tarea import Tarea


def tarea_item(tarea: Tarea) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.button(
                rx.cond(tarea.completada, "Done", "Pending"),
                on_click=lambda: Estado.completar_tarea(tarea.id),
            ),
            rx.text(tarea.titulo, flex="1"),
            rx.button("X", on_click=lambda: Estado.eliminar_tarea(tarea.id)),
        ),
        padding="3",
        bg="white",
        border="1px solid",
        border_color="gray.200",
    )


def dashboard_page() -> rx.Component:
    return rx.box(
        rx.box(
            rx.hstack(
                rx.heading("Mis Tareas", size="5"),
                rx.spacer(),
                rx.button("Cerrar Sesion", on_click=Estado.cerrar_sesion),
            ),
            padding="4",
            bg="white",
            border_bottom="1px solid",
            border_color="gray.200",
        ),
        rx.box(
            rx.hstack(
                rx.input(
                    placeholder="Nueva tarea...",
                    value=Estado.titulo,
                    on_change=Estado.set_titulo,
                    flex="1",
                ),
                rx.button("Agregar", on_click=Estado.crear_tarea),
            ),
            padding="4",
            bg="gray.50",
        ),
        rx.hstack(
            rx.button(
                "Todas",
                on_click=lambda: Estado.cambiar_filtro("todas"),
                variant="outline",
            ),
            rx.button(
                "Pendientes",
                on_click=lambda: Estado.cambiar_filtro("pendientes"),
                variant="outline",
            ),
            rx.button(
                "Completadas",
                on_click=lambda: Estado.cambiar_filtro("completadas"),
                variant="outline",
            ),
            padding="4",
        ),
        rx.box(
            rx.foreach(Estado.tareas, tarea_item),
            padding="4",
            spacing="3",
        ),
        min_height="100vh",
        bg="gray.50",
    )
