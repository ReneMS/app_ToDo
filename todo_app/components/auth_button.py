"""
Componente de botón de autenticación.
"""

import reflex as rx
from todo_app.states.estado import Estado


def cerrar():
    Estado.cerrar_sesion()


def AuthButton() -> rx.Component:
    """Botón de autenticación según el estado."""
    return rx.cond(
        Estado.esta_autenticado,
        rx.button(
            rx.icon(tag="log_out"),
            "Cerrar Sesión",
            variant="outline",
            color_scheme="red",
            size="sm",
            on_click=cerrar,
        ),
        rx.link(
            rx.button("Iniciar Sesión"),
            href="/login",
        ),
    )
