"""
Componente de tarjeta de tarea - Simplificado.
"""

import reflex as rx
from todo_app.states.estado import Estado


def completar(tarea_id: int):
    Estado.completar_tarea(tarea_id)


def eliminar(tarea_id: int):
    Estado.eliminar_tarea(tarea_id)


def TaskCard(
    tarea_id: int, titulo: str, descripcion: str, prioridad: str, completada: bool
) -> rx.Component:
    """Componente que renderiza una tarea individual."""
    colores = {
        "alta": "border-l-red-500",
        "media": "border-l-yellow-500",
        "baja": "border-l-green-500",
    }

    color = colores.get(prioridad, "border-l-gray-300")

    return rx.box(
        rx.hstack(
            rx.cond(
                completada,
                rx.button(
                    rx.icon(tag="check"),
                    on_click=lambda: completar(tarea_id),
                    class_name="w-6 h-6 rounded-full bg-green-500 text-white flex items-center justify-center",
                ),
                rx.button(
                    rx.box(class_name="w-5 h-5 rounded-full border-2 border-gray-300"),
                    on_click=lambda: completar(tarea_id),
                    class_name="w-6 h-6 flex items-center justify-center",
                ),
            ),
            rx.box(
                rx.vstack(
                    rx.cond(
                        completada,
                        rx.text(
                            titulo, class_name="line-through text-gray-400 font-medium"
                        ),
                        rx.text(titulo, class_name="font-medium text-gray-800"),
                    ),
                    rx.cond(
                        descripcion,
                        rx.text(descripcion, class_name="text-sm text-gray.500"),
                    ),
                    align_items="start",
                    spacing="1",
                ),
                flex="1",
            ),
            rx.hstack(
                rx.button(
                    rx.icon(tag="trash_2", class_name="w-4 h-4"),
                    size="sm",
                    variant="ghost",
                    color_scheme="red",
                    on_click=lambda: eliminar(tarea_id),
                ),
                spacing="1",
            ),
            spacing="3",
            align="start",
        ),
        class_name=f"p-4 bg-white rounded-lg border border-gray-200 border-l-4 {color} hover:shadow-md",
    )
