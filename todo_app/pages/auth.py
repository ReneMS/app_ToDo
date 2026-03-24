"""
Paginas de autenticacion - Diseño con Radix Themes.
"""

import reflex as rx
from todo_app.states.estado import Estado


def login_page() -> rx.Component:
    return rx.box(
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading("Bienvenido", size="8", font_weight="bold"),
                    rx.text("Inicia sesion", size="2"),
                    rx.box(
                        rx.vstack(
                            rx.text("Usuario o email", size="1", font_weight="medium"),
                            rx.input(
                                placeholder="tu@email.com",
                                value=Estado.login_username,
                                on_change=Estado.set_login_username,
                                width="100%",
                            ),
                            spacing="1",
                        ),
                        width="100%",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("Contrasena", size="1", font_weight="medium"),
                            rx.input(
                                type="password",
                                placeholder="********",
                                value=Estado.login_password,
                                on_change=Estado.set_login_password,
                                width="100%",
                            ),
                            spacing="1",
                        ),
                        width="100%",
                    ),
                    rx.button(
                        "Iniciar sesion",
                        on_click=Estado.iniciar_sesion,
                        width="100%",
                        color_scheme="indigo",
                    ),
                    rx.cond(
                        Estado.mensaje_error != "",
                        rx.box(
                            rx.text(Estado.mensaje_error, color_scheme="red", size="1"),
                            width="100%",
                            p="2",
                            bg="red",
                            border_radius="md",
                        ),
                    ),
                    rx.hstack(
                        rx.text("No tienes cuenta?"),
                        rx.link("Registrate", href="/register", color_scheme="indigo"),
                        spacing="2",
                        justify="center",
                        mt="4",
                    ),
                    spacing="4",
                ),
                width="100%",
                max_width="350px",
                p="6",
                border_radius="lg",
            ),
        ),
        min_height="100vh",
    )


def register_page() -> rx.Component:
    return rx.box(
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading("Crear cuenta", size="8", font_weight="bold"),
                    rx.text("Registrate gratis", size="2"),
                    rx.hstack(
                        rx.box(
                            rx.vstack(
                                rx.text("Nombre", size="1", font_weight="medium"),
                                rx.input(
                                    placeholder="Juan",
                                    value=Estado.register_nombre,
                                    on_change=Estado.set_register_nombre,
                                    width="100%",
                                ),
                                spacing="1",
                            ),
                            flex="1",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.text("Usuario", size="1", font_weight="medium"),
                                rx.input(
                                    placeholder="juan123",
                                    value=Estado.register_username,
                                    on_change=Estado.set_register_username,
                                    width="100%",
                                ),
                                spacing="1",
                            ),
                            flex="1",
                        ),
                        spacing="3",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("Email", size="1", font_weight="medium"),
                            rx.input(
                                type="email",
                                placeholder="tu@email.com",
                                value=Estado.register_email,
                                on_change=Estado.set_register_email,
                                width="100%",
                            ),
                            spacing="1",
                        ),
                        width="100%",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("Contrasena", size="1", font_weight="medium"),
                            rx.input(
                                type="password",
                                placeholder="********",
                                value=Estado.register_password,
                                on_change=Estado.set_register_password,
                                width="100%",
                            ),
                            spacing="1",
                        ),
                        width="100%",
                    ),
                    rx.button(
                        "Crear cuenta",
                        on_click=Estado.registrar,
                        width="100%",
                        color_scheme="indigo",
                    ),
                    rx.cond(
                        Estado.mensaje_error != "",
                        rx.box(
                            rx.text(Estado.mensaje_error, color_scheme="red", size="1"),
                            width="100%",
                            p="2",
                            bg="red",
                            border_radius="md",
                        ),
                    ),
                    rx.hstack(
                        rx.text("Ya tienes cuenta?"),
                        rx.link("Inicia sesion", href="/login", color_scheme="indigo"),
                        spacing="2",
                        justify="center",
                        mt="4",
                    ),
                    spacing="4",
                ),
                width="100%",
                max_width="400px",
                p="6",
                border_radius="lg",
            ),
        ),
        min_height="100vh",
    )
