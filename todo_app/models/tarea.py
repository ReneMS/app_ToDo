"""
Modelo de Tarea para el sistema ToDo.

Este módulo define la estructura de la tabla de tareas en la base de datos.
Cada tarea pertenece a un usuario específico.
"""

from datetime import datetime
from typing import Optional
import reflex as rx
from sqlmodel import Field, SQLModel, Relationship
from .usuario import Usuario


class Tarea(rx.Model, table=True):
    """
    Modelo de tarea para el sistema de gestión de tareas.

    Attributes:
        id: Identificador único de la tarea
        titulo: Título o nombre de la tarea
        descripcion: Descripción detallada de la tarea
        completada: Indica si la tarea está marcada como completada
        prioridad: Nivel de prioridad de la tarea (baja, media, alta)
        fecha_creacion: Fecha y hora de creación de la tarea
        fecha_limite: Fecha límite para completar la tarea
        fecha_completado: Fecha cuando se marcó como completada
        usuario_id: ID del usuario propietario de la tarea
    """

    # Campos de la tabla
    id: Optional[int] = Field(
        default=None, primary_key=True, description="Identificador único de la tarea"
    )

    titulo: str = Field(max_length=200, index=True, description="Título de la tarea")

    descripcion: Optional[str] = Field(
        default=None, description="Descripción detallada de la tarea"
    )

    completada: bool = Field(
        default=False, index=True, description="Indica si la tarea está completada"
    )

    prioridad: str = Field(
        default="media",
        max_length=20,
        index=True,
        description="Prioridad de la tarea: baja, media, alta",
    )

    fecha_creacion: datetime = Field(
        default_factory=datetime.now, description="Fecha de creación de la tarea"
    )

    fecha_limite: Optional[datetime] = Field(
        default=None, description="Fecha límite para completar la tarea"
    )

    fecha_completado: Optional[datetime] = Field(
        default=None, description="Fecha cuando se completó la tarea"
    )

    # Foreign Key al usuario
    usuario_id: int = Field(
        foreign_key="usuario.id", index=True, description="ID del usuario propietario"
    )

    def __repr__(self) -> str:
        """Representación legible de la tarea."""
        return (
            f"<Tarea(id={self.id}, titulo={self.titulo}, completada={self.completada})>"
        )

    def completar(self) -> None:
        """Marca la tarea como completada."""
        self.completada = True
        self.fecha_completado = datetime.now()

    def desmarcar(self) -> None:
        """Desmarca la tarea como completada."""
        self.completada = False
        self.fecha_completado = None
