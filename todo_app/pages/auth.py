"""
Paginas de autenticacion (Login y Registro).
"""

import reflex as rx
from todo_app.states.estado import Estado


class LoginState(rx.State):
    username: str = ""
    password: str = ""
    auto_setters = True

    def submit(self):
        Estado.iniciar_sesion(self.username, self.password)


class RegisterState(rx.State):
    username: str = ""
    email: str = ""
    password: str = ""
    nombre: str = ""
    auto_setters = True

    def submit(self):
        Estado.registrar(self.username, self.email, self.password, self.nombre)


def login_page() -> rx.Component:
    return rx.box(
        rx.box(
            rx.container(
                rx.hstack(
                    rx.link(
                        rx.heading(
                            "TaskFlow",
                            size="6",
                            font_weight="bold",
                            bg_gradient="linear(to-r, blue.600, purple.600)",
                            bg_clip="text",
                        ),
                        href="/",
                    ),
                    rx.spacer(),
                    rx.text("¿No tienes cuenta?", color="gray.500"),
                    rx.link(
                        "Registrate",
                        href="/register",
                        color="blue.600",
                        font_weight="medium",
                    ),
                    spacing="4",
                    align="center",
                ),
                padding_y="6",
                max_width="1200px",
                margin="0 auto",
            ),
            bg="white",
            border_bottom="1px solid",
            border_color="gray.100",
            position="relative",
            z_index="10",
        ),
        rx.box(
            rx.center(
                rx.box(
                    rx.vstack(
                        rx.vstack(
                            rx.heading(
                                "Bienvenido de nuevo",
                                size="7",
                                font_weight="bold",
                                color="gray.800",
                            ),
                            rx.text(
                                "Inicia sesion para continuar",
                                color="gray.500",
                                font_size="lg",
                            ),
                            spacing="2",
                            align="center",
                            padding_bottom="8",
                        ),
                        rx.vstack(
                            rx.text(
                                "Usuario o Email",
                                font_weight="medium",
                                color="gray.700",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="tu@email.com",
                                value=LoginState.username,
                                on_change=LoginState.set_username,
                                size="3",
                                bg="gray.50",
                                border="1px solid",
                                border_color="gray.200",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Contrasena",
                                font_weight="medium",
                                color="gray.700",
                                width="100%",
                            ),
                            rx.input(
                                type="password",
                                placeholder="********",
                                value=LoginState.password,
                                on_change=LoginState.set_password,
                                size="3",
                                bg="gray.50",
                                border="1px solid",
                                border_color="gray.200",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.hstack(
                            rx.checkbox(default_checked=False, color_scheme="blue"),
                            rx.text("Recordarme", color="gray.600"),
                            rx.spacer(),
                            rx.link(
                                "¿Olvidaste tu contrasena?",
                                href="#",
                                color="blue.600",
                                font_size="sm",
                            ),
                            width="100%",
                        ),
                        rx.button(
                            "Iniciar Sesion",
                            on_click=LoginState.submit,
                            size="3",
                            width="100%",
                            bg="blue.600",
                            color="white",
                            font_weight="semibold",
                        ),
                        rx.cond(
                            Estado.mensaje_error != "",
                            rx.box(
                                rx.text(
                                    Estado.mensaje_error,
                                    color="red.500",
                                    font_size="sm",
                                ),
                                bg="red.50",
                                padding="3",
                                border_radius="md",
                                width="100%",
                            ),
                        ),
                        spacing="6",
                        width="100%",
                        max_width="400px",
                    ),
                    bg="white",
                    padding="10",
                    border_radius="2xl",
                    box_shadow="2xl",
                    width="100%",
                    max_width="450px",
                ),
                min_height="calc(100vh - 80px)",
            ),
            bg="gray.50",
        ),
        min_height="100vh",
        bg="white",
    )


def register_page() -> rx.Component:
    return rx.box(
        rx.box(
            rx.container(
                rx.hstack(
                    rx.link(
                        rx.heading(
                            "TaskFlow",
                            size="6",
                            font_weight="bold",
                            bg_gradient="linear(to-r, blue.600, purple.600)",
                            bg_clip="text",
                        ),
                        href="/",
                    ),
                    rx.spacer(),
                    rx.text("¿Ya tienes cuenta?", color="gray.500"),
                    rx.link(
                        "Inicia sesion",
                        href="/login",
                        color="blue.600",
                        font_weight="medium",
                    ),
                    spacing="4",
                    align="center",
                ),
                padding_y="6",
                max_width="1200px",
                margin="0 auto",
            ),
            bg="white",
            border_bottom="1px solid",
            border_color="gray.100",
            position="relative",
            z_index="10",
        ),
        rx.box(
            rx.center(
                rx.box(
                    rx.vstack(
                        rx.vstack(
                            rx.heading(
                                "Crear cuenta",
                                size="7",
                                font_weight="bold",
                                color="gray.800",
                            ),
                            rx.text(
                                "Comienza a organizar tus tareas",
                                color="gray.500",
                                font_size="lg",
                            ),
                            spacing="2",
                            align="center",
                            padding_bottom="8",
                        ),
                        rx.hstack(
                            rx.vstack(
                                rx.text(
                                    "Nombre",
                                    font_weight="medium",
                                    color="gray.700",
                                    width="100%",
                                ),
                                rx.input(
                                    placeholder="Juan Perez",
                                    value=RegisterState.nombre,
                                    on_change=RegisterState.set_nombre,
                                    size="3",
                                    bg="gray.50",
                                    border="1px solid",
                                    border_color="gray.200",
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text(
                                    "Usuario",
                                    font_weight="medium",
                                    color="gray.700",
                                    width="100%",
                                ),
                                rx.input(
                                    placeholder="juan123",
                                    value=RegisterState.username,
                                    on_change=RegisterState.set_username,
                                    size="3",
                                    bg="gray.50",
                                    border="1px solid",
                                    border_color="gray.200",
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            spacing="4",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Email",
                                font_weight="medium",
                                color="gray.700",
                                width="100%",
                            ),
                            rx.input(
                                type="email",
                                placeholder="tu@email.com",
                                value=RegisterState.email,
                                on_change=RegisterState.set_email,
                                size="3",
                                bg="gray.50",
                                border="1px solid",
                                border_color="gray.200",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Contrasena",
                                font_weight="medium",
                                color="gray.700",
                                width="100%",
                            ),
                            rx.input(
                                type="password",
                                placeholder="********",
                                value=RegisterState.password,
                                on_change=RegisterState.set_password,
                                size="3",
                                bg="gray.50",
                                border="1px solid",
                                border_color="gray.200",
                            ),
                            rx.text(
                                "Minimo 6 caracteres",
                                font_size="xs",
                                color="gray.400",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.button(
                            "Crear Cuenta",
                            on_click=RegisterState.submit,
                            size="3",
                            width="100%",
                            bg="blue.600",
                            color="white",
                            font_weight="semibold",
                        ),
                        rx.cond(
                            Estado.mensaje_error != "",
                            rx.box(
                                rx.text(
                                    Estado.mensaje_error,
                                    color="red.500",
                                    font_size="sm",
                                ),
                                bg="red.50",
                                padding="3",
                                border_radius="md",
                                width="100%",
                            ),
                        ),
                        spacing="6",
                        width="100%",
                        max_width="400px",
                    ),
                    bg="white",
                    padding="10",
                    border_radius="2xl",
                    box_shadow="2xl",
                    width="100%",
                    max_width="450px",
                ),
                min_height="calc(100vh - 80px)",
            ),
            bg="gray.50",
        ),
        min_height="100vh",
        bg="white",
    )
