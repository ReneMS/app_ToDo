"""
Landing Page TaskFlow.
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
            rx.container(
                rx.hstack(
                    rx.heading("TaskFlow", size="6", font_weight="bold", color="white"),
                    rx.spacer(),
                    rx.hstack(
                        rx.link(
                            rx.button("Iniciar", variant="ghost", color="white"),
                            href="/login",
                        ),
                        rx.link(
                            rx.button("Registrarse", bg="blue.600", color="white"),
                            href="/register",
                        ),
                    ),
                ),
                max_width="1200px",
                py="4",
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
                top="10%",
                left="5%",
                width="500px",
                height="500px",
                border_radius="full",
                bg="rgba(99,102,241,0.1)",
                filter="blur(100px)",
            ),
            rx.box(
                position="absolute",
                bottom="10%",
                right="5%",
                width="600px",
                height="600px",
                border_radius="full",
                bg="rgba(168,85,247,0.08)",
                filter="blur(120px)",
            ),
            rx.center(
                rx.vstack(
                    rx.box(
                        rx.text("Version con IA", font_size="sm", color="blue.300"),
                        bg="whiteAlpha.100",
                        border_radius="full",
                        px="4",
                        py="2",
                    ),
                    rx.heading(
                        "Organiza tu vida", size="9", font_weight="bold", color="white"
                    ),
                    rx.heading(
                        "con inteligencia",
                        size="9",
                        font_weight="bold",
                        bg_gradient="linear(to-r, blue.400, purple.400)",
                        bg_clip="text",
                    ),
                    rx.text(
                        "TaskFlow te ayuda a gestionar tus tareas diarias.",
                        font_size="lg",
                        color="gray.400",
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "Comenzar Gratis",
                                size="3",
                                bg="blue.600",
                                color="white",
                            ),
                            href="/register",
                        ),
                        rx.link(
                            rx.button(
                                "Ver Demo",
                                size="3",
                                variant="outline",
                                color="white",
                                border_color="gray.600",
                            ),
                            href="/login",
                        ),
                        spacing="4",
                    ),
                    spacing="6",
                    max_width="700px",
                ),
                min_height="100vh",
                z_index="10",
            ),
            position="relative",
            min_height="100vh",
            bg="linear-gradient(180deg, #0f172a 0%, #1e1b4b 100%)",
        ),
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading(
                        "Por que TaskFlow?", size="8", font_weight="bold", color="white"
                    ),
                    rx.grid(
                        rx.box(
                            rx.vstack(
                                rx.heading("IA", size="5", color="white"),
                                rx.text("Analisis inteligente", color="gray.400"),
                                spacing="3",
                            ),
                            bg="gray.800",
                            border_radius="xl",
                            p="8",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.heading("Rapido", size="5", color="white"),
                                rx.text("Optimizado", color="gray.400"),
                                spacing="3",
                            ),
                            bg="gray.800",
                            border_radius="xl",
                            p="8",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.heading("Seguro", size="5", color="white"),
                                rx.text("Datos protegidos", color="gray.400"),
                                spacing="3",
                            ),
                            bg="gray.800",
                            border_radius="xl",
                            p="8",
                        ),
                        columns="3",
                        spacing="6",
                    ),
                    spacing="8",
                ),
                max_width="1200px",
            ),
            bg="gray.950",
            py="16",
        ),
        rx.box(
            rx.container(
                rx.hstack(
                    rx.text("2026 TaskFlow", color="gray.500"),
                    rx.spacer(),
                    rx.text("Python + Reflex", color="gray.600"),
                ),
                max_width="1200px",
            ),
            bg="gray.950",
            py="6",
            border_top="1px solid",
            border_color="gray.800",
        ),
    )


app.add_page(index, route="/")
