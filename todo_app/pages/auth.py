"""
Paginas de autenticacion (Login y Registro) - Diseño moderno 2026.
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
            rx.box(
                rx.box(
                    class_name="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC4wNSI+PGNpcmNsZSBjeD0iMzAiIGN5PSIzMCIgcj0iMiIvPjwvZz48L2c+PC9zdmc+')] opacity-50",
                ),
                rx.box(
                    rx.heading(
                        "TaskFlow",
                        size="9",
                        font_weight="bold",
                        class_name="mb-4 text-white",
                    ),
                    rx.text(
                        "Organiza tu vida con IA",
                        class_name="text-xl text-white/80 mb-8",
                    ),
                    rx.box(
                        rx.box(
                            rx.text("⚡", class_name="text-2xl"),
                            class_name="w-12 h-12 rounded-full bg-white/20 flex items-center justify-center",
                        ),
                        rx.box(
                            rx.text("🔒", class_name="text-2xl"),
                            class_name="w-12 h-12 rounded-full bg-white/20 flex items-center justify-center",
                        ),
                        rx.box(
                            rx.text("🎯", class_name="text-2xl"),
                            class_name="w-12 h-12 rounded-full bg-white/20 flex items-center justify-center",
                        ),
                        class_name="flex gap-4",
                    ),
                    rx.text(
                        "Únete a miles de usuarios", class_name="mt-8 text-white/60"
                    ),
                    class_name="relative z-10 flex flex-col justify-center px-12 text-white",
                ),
                class_name="hidden lg:flex lg:w-1/2 bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-500 relative overflow-hidden",
            ),
            rx.box(
                rx.box(
                    rx.heading(
                        "TaskFlow",
                        size="8",
                        font_weight="bold",
                        class_name="text-white text-center lg:hidden mb-8",
                    ),
                    rx.heading(
                        "Bienvenido de nuevo",
                        size="8",
                        font_weight="bold",
                        class_name="text-white mb-2",
                    ),
                    rx.text(
                        "Inicia sesión en tu cuenta", class_name="text-slate-400 mb-8"
                    ),
                    rx.box(
                        rx.text(
                            "Email o usuario",
                            class_name="text-slate-300 text-sm font-medium mb-2",
                        ),
                        rx.input(
                            placeholder="tu@email.com",
                            value=LoginState.username,
                            on_change=LoginState.set_username,
                            class_name="w-full px-4 py-3.5 bg-slate-900/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500",
                        ),
                        class_name="space-y-5",
                    ),
                    rx.box(
                        rx.text(
                            "Contraseña",
                            class_name="text-slate-300 text-sm font-medium mb-2",
                        ),
                        rx.input(
                            type="password",
                            placeholder="••••••••",
                            value=LoginState.password,
                            on_change=LoginState.set_password,
                            class_name="w-full px-4 py-3.5 bg-slate-900/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500",
                        ),
                        class_name="space-y-5",
                    ),
                    rx.hstack(
                        rx.checkbox(default_checked=False, color_scheme="indigo"),
                        rx.text("Recordarme", class_name="text-slate-400 text-sm"),
                        rx.spacer(),
                        rx.link(
                            "¿Olvidaste tu contraseña?",
                            href="#",
                            class_name="text-indigo-400 text-sm",
                        ),
                        class_name="items-center",
                    ),
                    rx.button(
                        "Iniciar sesión",
                        on_click=LoginState.submit,
                        class_name="w-full py-3.5 bg-gradient-to-r from-indigo-600 to-purple-600 text-white font-semibold rounded-xl",
                    ),
                    rx.cond(
                        Estado.mensaje_error != "",
                        rx.box(
                            rx.text(
                                "⚠️ " + Estado.mensaje_error,
                                class_name="text-red-400 text-sm",
                            ),
                            class_name="p-4 bg-red-500/10 border border-red-500/20 rounded-xl",
                        ),
                    ),
                    rx.hstack(
                        rx.text("¿No tienes cuenta?", class_name="text-slate-400"),
                        rx.link(
                            "Regístrate gratis",
                            href="/register",
                            class_name="text-indigo-400 font-medium",
                        ),
                        class_name="mt-8 justify-center gap-2",
                    ),
                    class_name="w-full max-w-md space-y-5",
                ),
                class_name="w-full lg:w-1/2 flex items-center justify-center p-8",
            ),
            class_name="min-h-screen bg-slate-950 flex",
        ),
    )


def register_page() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.box(
                    class_name="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC4wNSI+PGNpcmNsZSBjeD0iMzAiIGN5PSIzMCIgcj0iMiIvPjwvZz48L2c+PC9zdmc+')] opacity-50",
                ),
                rx.box(
                    rx.heading(
                        "Únete a TaskFlow",
                        size="8",
                        font_weight="bold",
                        class_name="mb-4 text-white",
                    ),
                    rx.text(
                        "Empieza a organizar tus tareas hoy",
                        class_name="text-xl text-white/80 mb-8",
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.text("✓", class_name="text-green-400"),
                            rx.text("Gestión inteligente", class_name="text-white/80"),
                            spacing="3",
                        ),
                        rx.hstack(
                            rx.text("✓", class_name="text-green-400"),
                            rx.text("Análisis con IA", class_name="text-white/80"),
                            spacing="3",
                        ),
                        rx.hstack(
                            rx.text("✓", class_name="text-green-400"),
                            rx.text(
                                "Sincronización en la nube", class_name="text-white/80"
                            ),
                            spacing="3",
                        ),
                        spacing="3",
                    ),
                    class_name="relative z-10 flex flex-col justify-center px-12 text-white",
                ),
                class_name="hidden lg:flex lg:w-1/2 bg-gradient-to-br from-pink-500 via-purple-600 to-indigo-600 relative overflow-hidden",
            ),
            rx.box(
                rx.box(
                    rx.heading(
                        "TaskFlow",
                        size="8",
                        font_weight="bold",
                        class_name="text-white text-center lg:hidden mb-8",
                    ),
                    rx.heading(
                        "Crear cuenta",
                        size="8",
                        font_weight="bold",
                        class_name="text-white mb-2",
                    ),
                    rx.text(
                        "Completa tus datos para comenzar",
                        class_name="text-slate-400 mb-8",
                    ),
                    rx.box(
                        rx.box(
                            rx.text(
                                "Nombre completo",
                                class_name="text-slate-300 text-sm font-medium mb-2",
                            ),
                            rx.input(
                                placeholder="Juan Pérez",
                                value=RegisterState.nombre,
                                on_change=RegisterState.set_nombre,
                                class_name="w-full px-4 py-3.5 bg-slate-900/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500",
                            ),
                            class_name="flex-1",
                        ),
                        rx.box(
                            rx.text(
                                "Usuario",
                                class_name="text-slate-300 text-sm font-medium mb-2",
                            ),
                            rx.input(
                                placeholder="juan123",
                                value=RegisterState.username,
                                on_change=RegisterState.set_username,
                                class_name="w-full px-4 py-3.5 bg-slate-900/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500",
                            ),
                            class_name="flex-1",
                        ),
                        class_name="flex gap-4",
                    ),
                    rx.box(
                        rx.text(
                            "Email",
                            class_name="text-slate-300 text-sm font-medium mb-2",
                        ),
                        rx.input(
                            type="email",
                            placeholder="tu@email.com",
                            value=RegisterState.email,
                            on_change=RegisterState.set_email,
                            class_name="w-full px-4 py-3.5 bg-slate-900/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500",
                        ),
                        class_name="space-y-4",
                    ),
                    rx.box(
                        rx.text(
                            "Contraseña",
                            class_name="text-slate-300 text-sm font-medium mb-2",
                        ),
                        rx.input(
                            type="password",
                            placeholder="••••••••",
                            value=RegisterState.password,
                            on_change=RegisterState.set_password,
                            class_name="w-full px-4 py-3.5 bg-slate-900/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500",
                        ),
                        rx.text(
                            "Mínimo 6 caracteres", class_name="text-slate-500 text-xs"
                        ),
                        class_name="space-y-4",
                    ),
                    rx.button(
                        "Crear cuenta",
                        on_click=RegisterState.submit,
                        class_name="w-full py-3.5 bg-gradient-to-r from-pink-500 to-indigo-600 text-white font-semibold rounded-xl",
                    ),
                    rx.cond(
                        Estado.mensaje_error != "",
                        rx.box(
                            rx.text(
                                "⚠️ " + Estado.mensaje_error,
                                class_name="text-red-400 text-sm",
                            ),
                            class_name="p-4 bg-red-500/10 border border-red-500/20 rounded-xl",
                        ),
                    ),
                    rx.hstack(
                        rx.text("¿Ya tienes cuenta?", class_name="text-slate-400"),
                        rx.link(
                            "Inicia sesión",
                            href="/login",
                            class_name="text-indigo-400 font-medium",
                        ),
                        class_name="mt-8 justify-center gap-2",
                    ),
                    class_name="w-full max-w-md space-y-5",
                ),
                class_name="w-full lg:w-1/2 flex items-center justify-center p-8",
            ),
            class_name="min-h-screen bg-slate-950 flex",
        ),
    )
