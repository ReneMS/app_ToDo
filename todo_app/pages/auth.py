"""
Paginas de autenticacion (Login y Registro) - Diseño limpio.
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
            class_name="fixed top-0 left-0 right-0 z-50 bg-slate-900 border-b border-slate-700",
            rx.container(
                class_name="max-w-6xl mx-auto",
                rx.hstack(
                    rx.link(
                        rx.heading(
                            "TaskFlow",
                            size="6",
                            font_weight="bold",
                            class_name="text-white",
                        ),
                        href="/",
                    ),
                    rx.spacer(),
                    rx.text("¿No tienes cuenta?", class_name="text-slate-400"),
                    rx.link(
                        "Regístrate",
                        href="/register",
                        class_name="text-blue-400 font-medium hover:text-blue-300",
                    ),
                    class_name="py-4",
                ),
            ),
        ),
        rx.box(
            class_name="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-indigo-900 flex items-center justify-center p-4",
            rx.box(
                class_name="w-full max-w-md bg-slate-800 rounded-2xl shadow-2xl border border-slate-700 p-8",
                rx.vstack(
                    rx.heading(
                        "Bienvenido de nuevo",
                        size="8",
                        font_weight="bold",
                        class_name="text-white text-center",
                    ),
                    rx.text(
                        "Inicia sesión para continuar",
                        class_name="text-slate-400 text-center mb-6",
                    ),
                    rx.box(
                        class_name="w-full",
                        rx.vstack(
                            rx.text("Usuario o Email", class_name="text-slate-300 font-medium w-full mb-1"),
                            rx.input(
                                placeholder="tu@email.com",
                                value=LoginState.username,
                                on_change=LoginState.set_username,
                                class_name="w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500",
                            ),
                            class_name="w-full mb-4",
                        ),
                    ),
                    rx.box(
                        class_name="w-full",
                        rx.vstack(
                            rx.text("Contraseña", class_name="text-slate-300 font-medium w-full mb-1"),
                            rx.input(
                                type="password",
                                placeholder="********",
                                value=LoginState.password,
                                on_change=LoginState.set_password,
                                class_name="w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500",
                            ),
                            class_name="w-full mb-4",
                        ),
                    ),
                    rx.hstack(
                        rx.checkbox(default_checked=False, color_scheme="blue"),
                        rx.text("Recordarme", class_name="text-slate-400"),
                        rx.spacer(),
                        rx.link("¿Olvidaste tu contraseña?", href="#", class_name="text-blue-400 text-sm hover:text-blue-300"),
                        class_name="w-full mb-4",
                    ),
                    rx.button(
                        "Iniciar Sesión",
                        on_click=LoginState.submit,
                        class_name="w-full py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-500 transition-colors",
                    ),
                    rx.cond(
                        Estado.mensaje_error != "",
                        rx.box(
                            rx.text(Estado.mensaje_error, class_name="text-red-300 text-sm"),
                            class_name="w-full p-3 bg-red-900/50 rounded-lg mt-4",
                        ),
                    ),
                    spacing="4",
                ),
            ),
        ),
    )


def register_page() -> rx.Component:
    return rx.box(
        rx.box(
            class_name="fixed top-0 left-0 right-0 z-50 bg-slate-900 border-b border-slate-700",
            rx.container(
                class_name="max-w-6xl mx-auto",
                rx.hstack(
                    rx.link(
                        rx.heading(
                            "TaskFlow",
                            size="6",
                            font_weight="bold",
                            class_name="text-white",
                        ),
                        href="/",
                    ),
                    rx.spacer(),
                    rx.text("¿Ya tienes cuenta?", class_name="text-slate-400"),
                    rx.link(
                        "Inicia sesión",
                        href="/login",
                        class_name="text-blue-400 font-medium hover:text-blue-300",
                    ),
                    class_name="py-4",
                ),
            ),
        ),
        rx.box(
            class_name="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-indigo-900 flex items-center justify-center p-4",
            rx.box(
                class_name="w-full max-w-md bg-slate-800 rounded-2xl shadow-2xl border border-slate-700 p-8",
                rx.vstack(
                    rx.heading(
                        "Crear cuenta",
                        size="8",
                        font_weight="bold",
                        class_name="text-white text-center",
                    ),
                    rx.text(
                        "Comienza a organizar tus tareas",
                        class_name="text-slate-400 text-center mb-6",
                    ),
                    rx.hstack(
                        rx.box(
                            rx.vstack(
                                rx.text("Nombre", class_name="text-slate-300 font-medium w-full mb-1"),
                                rx.input(
                                    placeholder="Juan Perez",
                                    value=RegisterState.nombre,
                                    on_change=RegisterState.set_nombre,
                                    class_name="w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500",
                                ),
                                class_name="w-full",
                            ),
                            class_name="flex-1",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.text("Usuario", class_name="text-slate-300 font-medium w-full mb-1"),
                                rx.input(
                                    placeholder="juan123",
                                    value=RegisterState.username,
                                    on_change=RegisterState.set_username,
                                    class_name="w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500",
                                ),
                                class_name="w-full",
                            ),
                            class_name="flex-1",
                        ),
                        class_name="w-full gap-4 mb-4",
                    ),
                    rx.box(
                        class_name="w-full",
                        rx.vstack(
                            rx.text("Email", class_name="text-slate-300 font-medium w-full mb-1"),
                            rx.input(
                                type="email",
                                placeholder="tu@email.com",
                                value=RegisterState.email,
                                on_change=RegisterState.set_email,
                                class_name="w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500",
                            ),
                            class_name="w-full mb-4",
                        ),
                    ),
                    rx.box(
                        class_name="w-full",
                        rx.vstack(
                            rx.text("Contraseña", class_name="text-slate-300 font-medium w-full mb-1"),
                            rx.input(
                                type="password",
                                placeholder="********",
                                value=RegisterState.password,
                                on_change=RegisterState.set_password,
                                class_name="w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500",
                            ),
                            rx.text("Mínimo 6 caracteres", class_name="text-slate-500 text-xs w-full"),
                            class_name="w-full mb-4",
                        ),
                    ),
                    rx.button(
                        "Crear Cuenta",
                        on_click=RegisterState.submit,
                        class_name="w-full py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-500 transition-colors",
                    ),
                    rx.cond(
                        Estado.mensaje_error != "",
                        rx.box(
                            rx.text(Estado.mensaje_error, class_name="text-red-300 text-sm"),
                            class_name="w-full p-3 bg-red-900/50 rounded-lg mt-4",
                        ),
                    ),
                    spacing="4",
                ),
            ),
        ),
    )
