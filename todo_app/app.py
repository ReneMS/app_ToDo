"""
Landing Page TaskFlow - Diseño simplificado.
"""

import reflex as rx
from todo_app.pages.auth import login_page, register_page
from todo_app.pages.dashboard import dashboard_page


app = rx.App()

app.add_page(login_page, route="/login")
app.add_page(register_page, route="/register")
app.add_page(dashboard_page, route="/dashboard")


def index() -> rx.Component:
    return rx.box(
        rx.box(
            rx.hstack(
                rx.heading("TaskFlow", size="7", font_weight="bold", color="white"),
                rx.spacer(),
                rx.link(rx.button("Iniciar sesion"), href="/login"),
                rx.link(
                    rx.button("Registrarse", color_scheme="blue"), href="/register"
                ),
                spacing="4",
            ),
            bg="gray.900",
            p="4",
            position="fixed",
            top="0",
            left="0",
            right="0",
            z_index="50",
        ),
        rx.box(
            rx.vstack(
                rx.heading(
                    "Organiza tu vida", size="9", font_weight="bold", color="white"
                ),
                rx.heading(
                    "con inteligencia", size="9", font_weight="bold", color="blue.400"
                ),
                rx.text(
                    "La mejor app de tareas con IA", color="gray.400", font_size="xl"
                ),
                rx.hstack(
                    rx.link(
                        rx.button("Comenzar Gratis", size="lg", color_scheme="blue"),
                        href="/register",
                    ),
                    rx.link(
                        rx.button("Ver Demo", size="lg", variant="outline"),
                        href="/login",
                    ),
                    spacing="4",
                ),
                spacing="6",
                align="center",
            ),
            min_height="80vh",
            bg="gray.950",
            color="white",
            pt="32",
        ),
        rx.box(
            rx.vstack(
                rx.heading(
                    "Por que TaskFlow?", size="8", font_weight="bold", color="white"
                ),
                rx.hstack(
                    rx.box(
                        rx.vstack(
                            rx.heading("IA", size="6", color="white"),
                            rx.text("Analisis inteligente", color="gray.400"),
                            spacing="2",
                        ),
                        bg="gray.800",
                        p="6",
                        border_radius="lg",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.heading("Rapido", size="6", color="white"),
                            rx.text("Optimizado", color="gray.400"),
                            spacing="2",
                        ),
                        bg="gray.800",
                        p="6",
                        border_radius="lg",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.heading("Seguro", size="6", color="white"),
                            rx.text("Datos protegidos", color="gray.400"),
                            spacing="2",
                        ),
                        bg="gray.800",
                        p="6",
                        border_radius="lg",
                    ),
                    spacing="6",
                ),
                spacing="8",
            ),
            bg="gray.900",
            p="12",
            color="white",
        ),
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "TaskFlow", size="5", font_weight="bold", color="white"
                            ),
                            rx.text(
                                "Tu app de tareas", color="gray.400", font_size="sm"
                            ),
                            spacing="2",
                        ),
                    ),
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "Producto",
                                size="4",
                                font_weight="semibold",
                                color="white",
                            ),
                            rx.link(
                                rx.text("Caracteristicas", color="gray.400"), href="#"
                            ),
                            rx.link(rx.text("Precios", color="gray.400"), href="#"),
                            spacing="2",
                        ),
                    ),
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "Legal", size="4", font_weight="semibold", color="white"
                            ),
                            rx.link(rx.text("Privacidad", color="gray.400"), href="#"),
                            rx.link(rx.text("Terminos", color="gray.400"), href="#"),
                            spacing="2",
                        ),
                    ),
                    spacing="16",
                    justify="around",
                    width="100%",
                ),
                rx.text("© 2026 TaskFlow", color="gray.500", font_size="sm", pt="8"),
                spacing="8",
            ),
            bg="gray.950",
            p="8",
            color="white",
        ),
    )


app.add_page(index, route="/")
