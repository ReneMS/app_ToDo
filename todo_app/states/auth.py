"""
Estado de autenticación del sistema.

Este módulo maneja el registro, inicio y cierre de sesión de usuarios.
"""

import reflex as rx
from passlib.context import CryptContext
from sqlmodel import select

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthState(rx.State):
    """Estado de autenticación para gestionar sesiones de usuarios."""

    usuario_id: int
    username: str = ""
    esta_autenticado: bool = False
    mensaje_error: str = ""

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verificar_password(password: str, password_hash: str) -> bool:
        return pwd_context.verify(password, password_hash)

    def iniciar_sesion(self, username: str, password: str) -> bool:
        from todo_app.models.usuario import Usuario

        self.mensaje_error = ""

        with rx.session() as session:
            usuario = session.exec(
                select(Usuario).where(
                    (Usuario.username == username) | (Usuario.email == username)
                )
            ).first()

            if usuario is None:
                self.mensaje_error = "Usuario no encontrado"
                return False

            if not usuario.activo:
                self.mensaje_error = "Usuario desactivado"
                return False

            if not self.verificar_password(password, usuario.password_hash):
                self.mensaje_error = "Contraseña incorrecta"
                return False

            self.usuario_id = usuario.id  # type: ignore
            self.username = usuario.username
            self.esta_autenticado = True

        return True

    def registrar_usuario(
        self, username: str, email: str, password: str, nombre: str
    ) -> bool:
        from todo_app.models.usuario import Usuario

        self.mensaje_error = ""

        if len(username) < 3:
            self.mensaje_error = "El usuario debe tener al menos 3 caracteres"
            return False

        if len(password) < 6:
            self.mensaje_error = "La contraseña debe tener al menos 6 caracteres"
            return False

        with rx.session() as session:
            usuario_existente = session.exec(
                select(Usuario).where(Usuario.username == username)
            ).first()

            if usuario_existente:
                self.mensaje_error = "El nombre de usuario ya está en uso"
                return False

            email_existente = session.exec(
                select(Usuario).where(Usuario.email == email)
            ).first()

            if email_existente:
                self.mensaje_error = "El correo electrónico ya está registrado"
                return False

            nuevo_usuario = Usuario(
                username=username,
                email=email,
                password_hash=self.hash_password(password),
                nombre=nombre,
                activo=True,
            )

            session.add(nuevo_usuario)
            session.commit()

            self.usuario_id = nuevo_usuario.id  # type: ignore
            self.username = nuevo_usuario.username
            self.esta_autenticado = True

        return True

    def cerrar_sesion(self) -> None:
        self.usuario_id = 0
        self.username = ""
        self.esta_autenticado = False
        self.mensaje_error = ""
