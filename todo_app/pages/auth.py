"""
Paginas de autenticacion (Login y Registro) - Diseño moderno.
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
                            color="white",
                        ),
                        href="/",
                    ),
                    rx.spacer(),
                    rx.text("¿No tienes cuenta?", color="gray.400"),
                    rx.link(
                        "Regístrate",
                        href="/register",
                        color="blue.400",
                        font_weight="medium",
                    ),
                    spacing="4",
                    align="center",
                ),
                padding_y="4",
                max_width="1200px",
                margin="0 auto",
            ),
            position="fixed",
            top="0",
            left="0",
            right="0",
            z_index="50",
            bg="rgba(15,23,42,0.95)",
            backdrop_filter="blur(10px)",
            border_bottom="1px solid",
            border_color="gray.800",
        ),
        rx.box(
            rx.box(
                position="absolute",
                top="20%",
                left="10%",
                width="400px",
                height="400px",
                border_radius="full",
                bg="rgba(99,102,241,0.15)",
                filter="blur(80px)",
            ),
            rx.box(
                position="absolute",
                bottom="20%",
                right="10%",
                width="500px",
                height="500px",
                border_radius="full",
                bg="rgba(168,85,247,0.1)",
                filter="blur(100px)",
            ),
            rx.center(
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.vstack(
                                rx.heading(
                                    "Bienvenido de nuevo",
                                    size="8",
                                    font_weight="bold",
                                    color="white",
                                ),
                                rx.text(
                                    "Inicia sesión para continuar",
                                    color="gray.400",
                                    font_size="lg",
                                ),
                                spacing="2",
                                align="center",
                            ),
                            width="100%",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.text(
                                    "Usuario o Email",
                                    font_weight="medium",
                                    color="gray.300",
                                    width="100%",
                                ),
                                rx.input(
                                    placeholder="tu@email.com",
                                    value=LoginState.username,
                                    on_change=LoginState.set_username,
                                    size="3",
                                    bg="whiteAlpha.100",
                                    border="1px solid",
                                    border_color="gray.600",
                                    color="white",
                                    _placeholder={"color": "gray.500"},
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            width="100%",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.text(
                                    "Contraseña",
                                    font_weight="medium",
                                    color="gray.300",
                                    width="100%",
                                ),
                                rx.input(
                                    type="password",
                                    placeholder="********",
                                    value=LoginState.password,
                                    on_change=LoginState.set_password,
                                    size="3",
                                    bg="whiteAlpha.100",
                                    border="1px solid",
                                    border_color="gray.600",
                                    color="white",
                                    _placeholder={"color": "gray.500"},
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            width="100%",
                        ),
                        rx.hstack(
                            rx.checkbox(default_checked=False, color_scheme="blue"),
                            rx.text("Recordarme", color="gray.400"),
                            rx.spacer(),
                            rx.link(
                                "¿Olvidaste tu contraseña?",
                                href="#",
                                color="blue.400",
                                font_size="sm",
                            ),
                            width="100%",
                        ),
                        rx.button(
                            "Iniciar Sesión",
                            on_click=LoginState.submit,
                            size="3",
                            width="100%",
                            bg="blue.600",
                            color="white",
                            font_weight="semibold",
                            _hover={"bg": "blue.500"},
                        ),
                        rx.cond(
                            Estado.mensaje_error != "",
                            rx.box(
                                rx.text(
                                    Estado.mensaje_error,
                                    color="red.300",
                                    font_size="sm",
                                ),
                                bg="red.900",
                                padding="3",
                                border_radius="md",
                                width="100%",
                            ),
                        ),
                        spacing="6",
                        width="100%",
                        max_width="400px",
                    ),
                    bg="rgba(30,41,59,0.8)",
                    backdrop_filter="blur(20px)",
                    padding="8",
                    border_radius="2xl",
                    border="1px solid",
                    border_color="gray.700",
                    box_shadow="2xl",
                    width="100%",
                    max_width="450px",
                ),
                min_height="100vh",
                z_index="10",
            ),
            position="relative",
            min_height="100vh",
            bg="linear-gradient(180deg, #0f172a 0%, #1e1b4b 100%)",
        ),
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
                            color="white",
                        ),
                        href="/",
                    ),
                    rx.spacer(),
                    rx.text("¿Ya tienes cuenta?", color="gray.400"),
                    rx.link(
                        "Inicia sesión",
                        href="/login",
                        color="blue.400",
                        font_weight="medium",
                    ),
                    spacing="4",
                    align="center",
                ),
                padding_y="4",
                max_width="1200px",
                margin="0 auto",
            ),
            position="fixed",
            top="0",
            left="0",
            right="0",
            z_index="50",
            bg="rgba(15,23,42,0.95)",
            backdrop_filter="blur(10px)",
            border_bottom="1px solid",
            border_color="gray.800",
        ),
        rx.box(
            rx.box(
                position="absolute",
                top="20%",
                right="10%",
                width="400px",
                height="400px",
                border_radius="full",
                bg="rgba(99,102,241,0.15)",
                filter="blur(80px)",
            ),
            rx.box(
                position="absolute",
                bottom="20%",
                left="10%",
                width="500px",
                height="500px",
                border_radius="full",
                bg="rgba(236,72,153,0.1)",
                filter="blur(100px)",
            ),
            rx.center(
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.vstack(
                                rx.heading(
                                    "Crear cuenta",
                                    size="8",
                                    font_weight="bold",
                                    color="white",
                                ),
                                rx.text(
                                    "Comienza a organizar tus tareas",
                                    color="gray.400",
                                    font_size="lg",
                                ),
                                spacing="2",
                                align="center",
                            ),
                            width="100%",
                        ),
                        rx.hstack(
                            rx.box(
                                rx.vstack(
                                    rx.text(
                                        "Nombre",
                                        font_weight="medium",
                                        color="gray.300",
                                        width="100%",
                                    ),
                                    rx.input(
                                        placeholder="Juan Perez",
                                        value=RegisterState.nombre,
                                        on_change=RegisterState.set_nombre,
                                        size="3",
                                        bg="whiteAlpha.100",
                                        border="1px solid",
                                        border_color="gray.600",
                                        color="white",
                                        _placeholder={"color": "gray.500"},
                                    ),
                                    spacing="2",
                                    width="100%",
                                ),
                                width="100%",
                            ),
                            rx.box(
                                rx.vstack(
                                    rx.text(
                                        "Usuario",
                                        font_weight="medium",
                                        color="gray.300",
                                        width="100%",
                                    ),
                                    rx.input(
                                        placeholder="juan123",
                                        value=RegisterState.username,
                                        on_change=RegisterState.set_username,
                                        size="3",
                                        bg="whiteAlpha.100",
                                        border="1px solid",
                                        border_color="gray.600",
                                        color="white",
                                        _placeholder={"color": "gray.500"},
                                    ),
                                    spacing="2",
                                    width="100%",
                                ),
                                width="100%",
                            ),
                            spacing="4",
                            width="100%",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.text(
                                    "Email",
                                    font_weight="medium",
                                    color="gray.300",
                                    width="100%",
                                ),
                                rx.input(
                                    type="email",
                                    placeholder="tu@email.com",
                                    value=RegisterState.email,
                                    on_change=RegisterState.set_email,
                                    size="3",
                                    bg="whiteAlpha.100",
                                    border="1px solid",
                                    border_color="gray.600",
                                    color="white",
                                    _placeholder={"color": "gray.500"},
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            width="100%",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.text(
                                    "Contraseña",
                                    font_weight="medium",
                                    color="gray.300",
                                    width="100%",
                                ),
                                rx.input(
                                    type="password",
                                    placeholder="********",
                                    value=RegisterState.password,
                                    on_change=RegisterState.set_password,
                                    size="3",
                                    bg="whiteAlpha.100",
                                    border="1px solid",
                                    border_color="gray.600",
                                    color="white",
                                    _placeholder={"color": "gray.500"},
                                ),
                                rx.text(
                                    "Mínimo 6 caracteres",
                                    font_size="xs",
                                    color="gray.500",
                                    width="100%",
                                ),
                                spacing="2",
                                width="100%",
                            ),
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
                            _hover={"bg": "blue.500"},
                        ),
                        rx.cond(
                            Estado.mensaje_error != "",
                            rx.box(
                                rx.text(
                                    Estado.mensaje_error,
                                    color="red.300",
                                    font_size="sm",
                                ),
                                bg="red.900",
                                padding="3",
                                border_radius="md",
                                width="100%",
                            ),
                        ),
                        spacing="6",
                        width="100%",
                        max_width="400px",
                    ),
                    bg="rgba(30,41,59,0.8)",
                    backdrop_filter="blur(20px)",
                    padding="8",
                    border_radius="2xl",
                    border="1px solid",
                    border_color="gray.700",
                    box_shadow="2xl",
                    width="100%",
                    max_width="450px",
                ),
                min_height="100vh",
                z_index="10",
            ),
            position="relative",
            min_height="100vh",
            bg="linear-gradient(180deg, #0f172a 0%, #1e1b4b 100%)",
        ),
    )
