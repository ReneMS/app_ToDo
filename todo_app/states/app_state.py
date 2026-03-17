"""
Estado único de la aplicación que combina autenticación y tareas.
"""

import reflex as rx
from passlib.context import CryptContext
from sqlmodel import select

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AppState(rx.State):
    """Estado único de la aplicación."""

    # Variables de autenticación
    usuario_id: int = 0
    username: str = ""
    esta_autenticado: bool = False
    mensaje_error: str = ""
    mensaje_exito: str = ""

    # Variables de tareas
    tareas: list = []
    filtro_actual: str = "todas"

    # Variables del formulario
    titulo_form: str = ""
    descripcion_form: str = ""
    prioridad_form: str = "media"
    fecha_limite_form: str = ""

    # === MÉTODOS DE AUTENTICACIÓN ===

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

            self.usuario_id = usuario.id
            self.username = usuario.username
            self.esta_autenticado = True

        self.cargar_tareas()
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

            self.usuario_id = nuevo_usuario.id
            self.username = nuevo_usuario.username
            self.esta_autenticado = True

        self.cargar_tareas()
        return True

    def cerrar_sesion(self) -> None:
        self.usuario_id = 0
        self.username = ""
        self.esta_autenticado = False
        self.mensaje_error = ""
        self.tareas = []

    # === MÉTODOS DE TAREA ===

    def cargar_tareas(self) -> None:
        if self.usuario_id == 0:
            self.tareas = []
            return

        from todo_app.models.tarea import Tarea

        with rx.session() as session:
            consulta = select(Tarea).where(Tarea.usuario_id == self.usuario_id)

            if self.filtro_actual == "pendientes":
                consulta = consulta.where(Tarea.completada == False)
            elif self.filtro_actual == "completadas":
                consulta = consulta.where(Tarea.completada == True)

            consulta = consulta.order_by(Tarea.fecha_creacion.desc())
            self.tareas = session.exec(consulta).all()

    def crear_tarea(self) -> bool:
        from todo_app.models.tarea import Tarea
        from datetime import datetime

        if self.usuario_id == 0:
            self.mensaje_error = "Debes iniciar sesión"
            return False

        self.mensaje_error = ""

        if not self.titulo_form.strip():
            self.mensaje_error = "El título es obligatorio"
            return False

        fecha_limite = None
        if self.fecha_limite_form:
            try:
                fecha_limite = datetime.fromisoformat(self.fecha_limite_form)
            except ValueError:
                self.mensaje_error = "Formato de fecha inválido"
                return False

        with rx.session() as session:
            nueva_tarea = Tarea(
                titulo=self.titulo_form.strip(),
                descripcion=self.descripcion_form.strip() or None,
                prioridad=self.prioridad_form,
                fecha_limite=fecha_limite,
                usuario_id=self.usuario_id,
                completada=False,
            )
            session.add(nueva_tarea)
            session.commit()

        self.limpiar_formulario()
        self.mensaje_exito = "Tarea creada"
        self.cargar_tareas()
        return True

    def completar_tarea(self, tarea_id: int) -> bool:
        from todo_app.models.tarea import Tarea
        from datetime import datetime

        if self.usuario_id == 0:
            return False

        with rx.session() as session:
            tarea = session.exec(
                select(Tarea).where(
                    Tarea.id == tarea_id, Tarea.usuario_id == self.usuario_id
                )
            ).first()

            if tarea:
                tarea.completada = not tarea.completada
                tarea.fecha_completado = datetime.now() if tarea.completada else None
                session.commit()
                self.mensaje_exito = "Tarea actualizada"

        self.cargar_tareas()
        return True

    def eliminar_tarea(self, tarea_id: int) -> bool:
        from todo_app.models.tarea import Tarea

        if self.usuario_id == 0:
            return False

        with rx.session() as session:
            tarea = session.exec(
                select(Tarea).where(
                    Tarea.id == tarea_id, Tarea.usuario_id == self.usuario_id
                )
            ).first()

            if tarea:
                session.delete(tarea)
                session.commit()
                self.mensaje_exito = "Tarea eliminada"

        self.cargar_tareas()
        return True

    def establecer_filtro(self, filtro: str) -> None:
        self.filtro_actual = filtro
        self.cargar_tareas()

    def limpiar_formulario(self) -> None:
        self.titulo_form = ""
        self.descripcion_form = ""
        self.prioridad_form = "media"
        self.fecha_limite_form = ""
        self.mensaje_error = ""
        self.mensaje_exito = ""
