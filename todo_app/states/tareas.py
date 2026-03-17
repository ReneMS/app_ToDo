"""
Estado de gestión de tareas - Versión simplificada.

Este módulo maneja todas las operaciones CRUD sobre las tareas.
"""

from datetime import datetime
import reflex as rx
from sqlmodel import select, func, desc, asc


class TaskState(rx.State):
    """Estado para gestionar las tareas del usuario."""

    # Variables de estado
    tareas: list = []
    filtro_actual: str = "todas"
    orden_actual: str = "fecha_creacion"
    mensaje_exito: str = ""
    mensaje_error: str = ""

    # Campos del formulario
    titulo_form: str = ""
    descripcion_form: str = ""
    prioridad_form: str = "media"
    fecha_limite_form: str = ""

    def cargar_tareas(self) -> None:
        """Carga las tareas del usuario actual."""
        usuario_id = self.get_usuario_id()
        if usuario_id == 0:
            self.tareas = []
            return

        from todo_app.models.tarea import Tarea

        with rx.session() as session:
            consulta = select(Tarea).where(Tarea.usuario_id == usuario_id)

            if self.filtro_actual == "pendientes":
                consulta = consulta.where(Tarea.completada == False)
            elif self.filtro_actual == "completadas":
                consulta = consulta.where(Tarea.completada == True)

            if self.orden_actual == "fecha_creacion":
                consulta = consulta.order_by(desc(Tarea.fecha_creacion))
            elif self.orden_actual == "fecha_limite":
                consulta = consulta.order_by(asc(Tarea.fecha_limite))
            elif self.orden_actual == "prioridad":
                consulta = consulta.order_by(desc(Tarea.prioridad))

            self.tareas = session.exec(consulta).all()

    def get_usuario_id(self) -> int:
        """Obtiene el ID del usuario desde el estado padre."""
        if hasattr(self, "usuario_id"):
            return self.usuario_id
        return 0

    def crear_tarea(self) -> bool:
        """Crea una nueva tarea."""
        usuario_id = self.get_usuario_id()
        if usuario_id == 0:
            self.mensaje_error = "Debes iniciar sesión"
            return False

        self.mensaje_error = ""

        if not self.titulo_form.strip():
            self.mensaje_error = "El título es obligatorio"
            return False

        from todo_app.models.tarea import Tarea

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
                usuario_id=usuario_id,
                completada=False,
            )
            session.add(nueva_tarea)
            session.commit()

        self.limpiar_formulario()
        self.mensaje_exito = "Tarea creada"
        self.cargar_tareas()
        return True

    def completar_tarea(self, tarea_id: int) -> bool:
        """Marca una tarea como completada/pendiente."""
        usuario_id = self.get_usuario_id()
        if usuario_id == 0:
            return False

        from todo_app.models.tarea import Tarea

        with rx.session() as session:
            tarea = session.exec(
                select(Tarea).where(
                    Tarea.id == tarea_id, Tarea.usuario_id == usuario_id
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
        """Elimina una tarea."""
        usuario_id = self.get_usuario_id()
        if usuario_id == 0:
            return False

        from todo_app.models.tarea import Tarea

        with rx.session() as session:
            tarea = session.exec(
                select(Tarea).where(
                    Tarea.id == tarea_id, Tarea.usuario_id == usuario_id
                )
            ).first()

            if tarea:
                session.delete(tarea)
                session.commit()
                self.mensaje_exito = "Tarea eliminada"

        self.cargar_tareas()
        return True

    def establecer_filtro(self, filtro: str) -> None:
        """Establece el filtro de tareas."""
        self.filtro_actual = filtro
        self.cargar_tareas()

    def establecer_orden(self, orden: str) -> None:
        """Establece el orden de las tareas."""
        self.orden_actual = orden
        self.cargar_tareas()

    def limpiar_formulario(self) -> None:
        """Limpia los campos del formulario."""
        self.titulo_form = ""
        self.descripcion_form = ""
        self.prioridad_form = "media"
        self.fecha_limite_form = ""
        self.mensaje_error = ""
        self.mensaje_exito = ""


class TareasState(TaskState):
    """Estado de tareas que hereda del estado de autenticación."""

    pass
