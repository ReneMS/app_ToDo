"""
Landing Page TaskFlow - Diseño con Radix Themes.
"""

import reflex as rx
from todo_app.pages.auth import login_page, register_page
from todo_app.pages.dashboard import dashboard_page


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accent_color="indigo",
        gray_color="slate",
    ),
)

app.add_page(login_page, route="/login")
app.add_page(register_page, route="/register")
app.add_page(dashboard_page, route="/dashboard")


def index() -> rx.Component:
    return rx.box(
        rx.box(
            rx.hstack(
                rx.heading("TaskFlow", size="7", font_weight="bold"),
                rx.spacer(),
                rx.link(rx.button("Iniciar sesion"), href="/login"),
                rx.link(
                    rx.button("Registrarse", color_scheme="indigo"), href="/register"
                ),
                spacing="4",
            ),
            p="4",
            position="fixed",
            top="0",
            left="0",
            right="0",
            z_index="50",
        ),
        rx.box(
            rx.vstack(
                rx.heading("Organiza tu vida", size="9", font_weight="bold"),
                rx.heading(
                    "con inteligencia", size="9", font_weight="bold", color="indigo"
                ),
                rx.text("La mejor app de tareas con IA", size="2"),
                rx.hstack(
                    rx.link(
                        rx.button("Comenzar Gratis", size="3", color_scheme="indigo"),
                        href="/register",
                    ),
                    rx.link(
                        rx.button("Ver Demo", size="3", variant="outline"),
                        href="/login",
                    ),
                    spacing="4",
                ),
                spacing="6",
                align="center",
            ),
            min_height="80vh",
            pt="32",
        ),
        rx.box(
            rx.vstack(
                rx.heading("Por que TaskFlow?", size="8", font_weight="bold"),
                rx.hstack(
                    rx.box(
                        rx.vstack(
                            rx.heading("IA", size="6"),
                            rx.text("Analisis inteligente"),
                            spacing="2",
                        ),
                        p="6",
                        border_radius="lg",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.heading("Rapido", size="6"),
                            rx.text("Optimizado"),
                            spacing="2",
                        ),
                        p="6",
                        border_radius="lg",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.heading("Seguro", size="6"),
                            rx.text("Datos protegidos"),
                            spacing="2",
                        ),
                        p="6",
                        border_radius="lg",
                    ),
                    spacing="6",
                ),
                spacing="8",
            ),
            p="12",
        ),
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.vstack(
                            rx.heading("TaskFlow", size="5", font_weight="bold"),
                            rx.text("Tu app de tareas", size="1"),
                            spacing="2",
                        )
                    ),
                    rx.box(
                        rx.vstack(
                            rx.heading("Producto", size="3", font_weight="semibold"),
                            rx.link("Caracteristicas", href="#"),
                            rx.link("Precios", href="#"),
                            spacing="2",
                        )
                    ),
                    rx.box(
                        rx.vstack(
                            rx.heading("Legal", size="3", font_weight="semibold"),
                            rx.link("Privacidad", href="#"),
                            rx.link("Terminos", href="#"),
                            spacing="2",
                        )
                    ),
                    spacing="9",
                    justify="between",
                    width="100%",
                ),
                rx.text("© 2026 TaskFlow", size="1", color_scheme="gray"),
                spacing="8",
            ),
            p="8",
        ),
    )


app.add_page(index, route="/")
