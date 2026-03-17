"""
Paginas de autenticacion - Diseño limpio con props nativas de Reflex.
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
        min_height="100vh",
        bg="gray.950",
        color="white",
        rx.center(
            rx.box(
                width="100%",
                max_width="400px",
                bg="gray.900",
                border_radius="xl",
                p="8",
                box_shadow="0 25px 50px -12px rgba(0, 0, 0, 0.5)",
                border="1px solid",
                border_color="gray.800",
                rx.vstack(
                    rx.heading("Bienvenido", size="8", font_weight="bold", color="white"),
                    rx.text("Inicia sesión", color="gray.400", font_size="lg"),
                    rx.box(
                        width="100%",
                        rx.text("Usuario o email", color="gray.300", font_size="sm", font_weight="medium", mb="2"),
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
                        mb="4",
                    ),
                    rx.box(
                        width="100%",
                        rx.text("Contraseña", color="gray.300", font_size="sm", font_weight="medium", mb="2"),
                        rx.input(
                            type="password",
                            placeholder="••••••••",
                            value=LoginState.password,
                            on_change=LoginState.set_password,
                            width="100%",
                            p="3",
                            bg="gray.800",
                            border="1px solid",
                            border_color="gray.700",
                            color="white",
                        ),
                        mb="4",
                    ),
                    rx.button(
                        "Iniciar sesión",
                        on_click=LoginState.submit,
                        width="100%",
                        p="3",
                        bg="indigo.600",
                        color="white",
                        border_radius="md",
                        font_weight="semibold",
                        _hover={"bg": "indigo.500"},
                    ),
                    rx.cond(
                        Estado.mensaje_error != "",
                        rx.box(
                            rx.text(Estado.mensaje_error, color="red.400", font_size="sm"),
                            width="100%",
                            mt="4",
                            p="3",
                            bg="red.900",
                            border_radius="md",
                        ),
                    ),
                    rx.hstack(
                        mt="6",
                        rx.text("¿No tienes cuenta?", color="gray.400"),
                        rx.link("Regístrate", href="/register", color="indigo.400", font_weight="medium"),
                        spacing="2",
                        justify="center",
                    ),
                    spacing="5",
                ),
            ),
        ),
    )


def register_page() -> rx.Component:
    return rx.box(
        min_height="100vh",
        bg="gray.950",
        color="white",
        rx.center(
            rx.box(
                width="100%",
                max_width="450px",
                bg="gray.900",
                border_radius="xl",
                p="8",
                box_shadow="0 25px 50px -12px rgba(0, 0, 0, 0.5)",
                border="1px solid",
                border_color="gray.800",
                rx.vstack(
                    rx.heading("Crear cuenta", size="8", font_weight="bold", color="white"),
                    rx.text("Regístrate gratis", color="gray.400", font_size="lg"),
                    rx.hstack(
                        width="100%",
                        rx.box(
                            rx.text("Nombre", color="gray.300", font_size="sm", font_weight="medium", mb="2"),
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
                            rx.text("Usuario", color="gray.300", font_size="sm", font_weight="medium", mb="2"),
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
                    ),
                    rx.box(
                        width="100%",
                        rx.text("Email", color="gray.300", font_size="sm", font_weight="medium", mb="2"),
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
                        mb="4",
                    ),
                    rx.box(
                        width="100%",
                        rx.text("Contraseña", color="gray.300", font_size="sm", font_weight="medium", mb="2"),
                        rx.input(
                            type="password",
                            placeholder="••••••••",
                            value=RegisterState.password,
                            on_change=RegisterState.set_password,
                            width="100%",
                            p="3",
                            bg="gray.800",
                            border="1px solid",
                            border_color="gray.700",
                            color="white",
                        ),
                        rx.text("Mínimo 6 caracteres", color="gray.500", font_size="xs", mt="1"),
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
                        _hover={"bg": "indigo.500"},
                    ),
                    rx.cond(
                        Estado.mensaje_error != "",
                        rx.box(
                            rx.text(Estado.mensaje_error, color="red.400", font_size="sm"),
                            width="100%",
                            mt="4",
                            p="3",
                            bg="red.900",
                            border_radius="md",
                        ),
                    ),
                    rx.hstack(
                        mt="6",
                        rx.text("¿Ya tienes cuenta?", color="gray.400"),
                        rx.link("Inicia sesión", href="/login", color="indigo.400", font_weight="medium"),
                        spacing="2",
                        justify="center",
                    ),
                    spacing="5",
                ),
            ),
        ),
    )
