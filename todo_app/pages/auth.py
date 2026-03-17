"""
Paginas de autenticacion - Diseño limpio.
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
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Bienvenido", size="8", font_weight="bold", color="white"
                    ),
                    rx.text("Inicia sesion", color="gray.400", font_size="lg"),
                    rx.box(
                        rx.text(
                            "Usuario o email",
                            color="gray.300",
                            font_size="sm",
                            font_weight="medium",
                            mb="2",
                        ),
                        rx.input(
                            placeholder="tu@email.com",
                            value=LoginState.username,
                            on_change=LoginState.set_username,
                            width="100%",
                            p="3",
                            bg="gray.800",
                            border="1px solid",
                            border_color="gray.700",
                            color="white",
                        ),
                        width="100%",
                        mb="4",
                    ),
                    rx.box(
                        rx.text(
                            "Contrasena",
                            color="gray.300",
                            font_size="sm",
                            font_weight="medium",
                            mb="2",
                        ),
                        rx.input(
                            type="password",
                            placeholder="********",
                            value=LoginState.password,
                            on_change=LoginState.set_password,
                            width="100%",
                            p="3",
                            bg="gray.800",
                            border="1px solid",
                            border_color="gray.700",
                            color="white",
                        ),
                        width="100%",
                        mb="4",
                    ),
                    rx.button(
                        "Iniciar sesion",
                        on_click=LoginState.submit,
                        width="100%",
                        p="3",
                        bg="indigo.600",
                        color="white",
                        border_radius="md",
                        font_weight="semibold",
                    ),
                    rx.cond(
                        Estado.mensaje_error != "",
                        rx.box(
                            rx.text(
                                Estado.mensaje_error, color="red.400", font_size="sm"
                            ),
                            width="100%",
                            mt="4",
                            p="3",
                            bg="red.900",
                            border_radius="md",
                        ),
                    ),
                    rx.hstack(
                        rx.text("No tienes cuenta?", color="gray.400"),
                        rx.link(
                            "Registrate",
                            href="/register",
                            color="indigo.400",
                            font_weight="medium",
                        ),
                        spacing="2",
                        justify="center",
                        mt="6",
                    ),
                    spacing="5",
                ),
                width="100%",
                max_width="400px",
                bg="gray.900",
                border_radius="xl",
                p="8",
                box_shadow="lg",
                border="1px solid",
                border_color="gray.800",
            ),
        ),
        min_height="100vh",
        bg="gray.950",
        color="white",
    )


def register_page() -> rx.Component:
    return rx.box(
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Crear cuenta", size="8", font_weight="bold", color="white"
                    ),
                    rx.text("Registrate gratis", color="gray.400", font_size="lg"),
                    rx.hstack(
                        rx.box(
                            rx.text(
                                "Nombre",
                                color="gray.300",
                                font_size="sm",
                                font_weight="medium",
                                mb="2",
                            ),
                            rx.input(
                                placeholder="Juan",
                                value=RegisterState.nombre,
                                on_change=RegisterState.set_nombre,
                                width="100%",
                                p="3",
                                bg="gray.800",
                                border="1px solid",
                                border_color="gray.700",
                                color="white",
                            ),
                            flex="1",
                        ),
                        rx.box(
                            rx.text(
                                "Usuario",
                                color="gray.300",
                                font_size="sm",
                                font_weight="medium",
                                mb="2",
                            ),
                            rx.input(
                                placeholder="juan123",
                                value=RegisterState.username,
                                on_change=RegisterState.set_username,
                                width="100%",
                                p="3",
                                bg="gray.800",
                                border="1px solid",
                                border_color="gray.700",
                                color="white",
                            ),
                            flex="1",
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    rx.box(
                        rx.text(
                            "Email",
                            color="gray.300",
                            font_size="sm",
                            font_weight="medium",
                            mb="2",
                        ),
                        rx.input(
                            type="email",
                            placeholder="tu@email.com",
                            value=RegisterState.email,
                            on_change=RegisterState.set_email,
                            width="100%",
                            p="3",
                            bg="gray.800",
                            border="1px solid",
                            border_color="gray.700",
                            color="white",
                        ),
                        width="100%",
                        mb="4",
                    ),
                    rx.box(
                        rx.text(
                            "Contrasena",
                            color="gray.300",
                            font_size="sm",
                            font_weight="medium",
                            mb="2",
                        ),
                        rx.input(
                            type="password",
                            placeholder="********",
                            value=RegisterState.password,
                            on_change=RegisterState.set_password,
                            width="100%",
                            p="3",
                            bg="gray.800",
                            border="1px solid",
                            border_color="gray.700",
                            color="white",
                        ),
                        rx.text(
                            "Minimo 6 caracteres",
                            color="gray.500",
                            font_size="xs",
                            mt="1",
                        ),
                        width="100%",
                        mb="4",
                    ),
                    rx.button(
                        "Crear cuenta",
                        on_click=RegisterState.submit,
                        width="100%",
                        p="3",
                        bg="indigo.600",
                        color="white",
                        border_radius="md",
                        font_weight="semibold",
                    ),
                    rx.cond(
                        Estado.mensaje_error != "",
                        rx.box(
                            rx.text(
                                Estado.mensaje_error, color="red.400", font_size="sm"
                            ),
                            width="100%",
                            mt="4",
                            p="3",
                            bg="red.900",
                            border_radius="md",
                        ),
                    ),
                    rx.hstack(
                        rx.text("Ya tienes cuenta?", color="gray.400"),
                        rx.link(
                            "Inicia sesion",
                            href="/login",
                            color="indigo.400",
                            font_weight="medium",
                        ),
                        spacing="2",
                        justify="center",
                        mt="6",
                    ),
                    spacing="5",
                ),
                width="100%",
                max_width="450px",
                bg="gray.900",
                border_radius="xl",
                p="8",
                box_shadow="lg",
                border="1px solid",
                border_color="gray.800",
            ),
        ),
        min_height="100vh",
        bg="gray.950",
        color="white",
    )
