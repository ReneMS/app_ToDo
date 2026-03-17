"""
Componente de barra de navegación (Navbar) - Simplificado.
"""

import reflex as rx
from todo_app.states.auth import AuthState


def Navbar() -> rx.Component:
    """Componente de navegación principal."""
    return rx.box(
        rx.container(
            rx.hstack(
                # Logo
                rx.link(
                    rx.hstack(
                        rx.icon(
                            tag="check_circle", class_name="text-2xl text-indigo-600"
                        ),
                        rx.text(
                            "ToDo App", class_name="text-xl font-bold text-gray-800"
                        ),
                        spacing="2",
                    ),
                    href="/",
                    _hover={"text-decoration": "none"},
                ),
                # Navegación
                rx.hstack(
                    rx.cond(
                        AuthState.esta_autenticado,
                        rx.link(
                            "Mis Tareas",
                            href="/dashboard",
                            class_name="text-gray-600 hover:text-indigo-600",
                        ),
                    ),
                    rx.link(
                        "Iniciar Sesión",
                        href="/login",
                        class_name="text-gray-600 hover:text-indigo-600",
                    ),
                    rx.link(
                        "Registrarse",
                        href="/register",
                        class_name="bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700",
                    ),
                    spacing="4",
                ),
                justify="between",
                align="center",
            ),
            class_name="max-w-7xl mx-auto px-4",
        ),
        class_name="fixed top-0 left-0 right-0 z-50 bg-white border-b border-gray-200 shadow-sm h-16",
    )
