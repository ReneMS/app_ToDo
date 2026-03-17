"""
Estado de la aplicación - Auth + Tareas.
"""

import reflex as rx
from typing import List
from passlib.context import CryptContext
from sqlmodel import select, desc

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Estado(rx.State):
    """Estado combinado de la aplicación."""

    # Auth
    usuario_id: int = 0
    username: str = ""
    esta_autenticado: bool = False
    mensaje_error: str = ""

    # Tareas
    tareas: list = []
    filtro: str = "todas"

    # Formulario
    titulo: str = ""
    descripcion: str = ""
    prioridad: str = "media"

    # Setters explícitos (requeridos en Reflex 0.8.9+)
    def set_titulo(self, value: str):
        self.titulo = value

    def set_descripcion(self, value: str):
        self.descripcion = value

    def set_prioridad(self, value: str):
        self.prioridad = value

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def verificar_password(self, password: str, password_hash: str) -> bool:
        return pwd_context.verify(password, password_hash)

    def iniciar_sesion(self, username: str, password: str):
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
                return

            if not usuario.activo:
                self.mensaje_error = "Usuario desactivado"
                return

            if not self.verificar_password(password, usuario.password_hash):
                self.mensaje_error = "Contraseña incorrecta"
                return

            self.usuario_id = usuario.id  # type: ignore
            self.username = usuario.username
            self.esta_autenticado = True

        self.cargar_tareas()
        rx.redirect("/dashboard")

    def registrar(self, username: str, email: str, password: str, nombre: str):
        from todo_app.models.usuario import Usuario

        self.mensaje_error = ""

        if len(username) < 3:
            self.mensaje_error = "Usuario debe tener al menos 3 caracteres"
            return

        with rx.session() as session:
            existe = session.exec(
                select(Usuario).where(Usuario.username == username)
            ).first()
            if existe:
                self.mensaje_error = "Usuario ya existe"
                return

            nuevo = Usuario(
                username=username,
                email=email,
                password_hash=self.hash_password(password),
                nombre=nombre,
            )
            session.add(nuevo)
            session.commit()

            self.usuario_id = nuevo.id  # type: ignore
            self.username = nuevo.username
            self.esta_autenticado = True

        self.cargar_tareas()
        rx.redirect("/dashboard")

    def cerrar_sesion(self):
        self.usuario_id = 0
        self.username = ""
        self.esta_autenticado = False
        self.tareas = []
        rx.redirect("/")

    def cargar_tareas(self):
        if self.usuario_id == 0:
            self.tareas = []
            return

        from todo_app.models.tarea import Tarea

        with rx.session() as session:
            q = select(Tarea).where(Tarea.usuario_id == self.usuario_id)

            if self.filtro == "pendientes":
                q = q.where(Tarea.completada == False)
            elif self.filtro == "completadas":
                q = q.where(Tarea.completada == True)

            q = q.order_by(desc(Tarea.fecha_creacion))
            self.tareas = list(session.exec(q).all())

    def crear_tarea(self):
        if self.usuario_id == 0:
            return

        if not self.titulo.strip():
            self.mensaje_error = "El título es obligatorio"
            return

        from todo_app.models.tarea import Tarea

        with rx.session() as session:
            tarea = Tarea(
                titulo=self.titulo.strip(),
                descripcion=self.descripcion.strip() or None,
                prioridad=self.prioridad,
                usuario_id=self.usuario_id,
            )
            session.add(tarea)
            session.commit()

        self.titulo = ""
        self.descripcion = ""
        self.prioridad = "media"
        self.cargar_tareas()

    def completar_tarea(self, tarea_id: int):
        if self.usuario_id == 0:
            return

        from todo_app.models.tarea import Tarea

        with rx.session() as session:
            tarea = session.exec(
                select(Tarea).where(
                    Tarea.id == tarea_id, Tarea.usuario_id == self.usuario_id
                )
            ).first()

            if tarea:
                tarea.completada = not tarea.completada
                session.commit()

        self.cargar_tareas()

    def eliminar_tarea(self, tarea_id: int):
        if self.usuario_id == 0:
            return

        from todo_app.models.tarea import Tarea

        with rx.session() as session:
            tarea = session.exec(
                select(Tarea).where(
                    Tarea.id == tarea_id, Tarea.usuario_id == self.usuario_id
                )
            ).first()

            if tarea:
                session.delete(tarea)
                session.commit()

        self.cargar_tareas()

    def cambiar_filtro(self, filtro: str):
        self.filtro = filtro
        self.cargar_tareas()
