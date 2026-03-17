"""
Modelo de Usuario para autenticación.

Este módulo define la estructura de la tabla de usuarios en la base de datos.
Utiliza SQLModel para combinar la funcionalidad de SQLAlchemy (ORM) y Pydantic (validación).
"""

from datetime import datetime
from typing import Optional
import reflex as rx
from sqlmodel import Field, SQLModel


class Usuario(rx.Model, table=True):
    """
    Modelo de usuario para la autenticación del sistema.

    Attributes:
        id: Identificador único del usuario
        username: Nombre de usuario único
        email: Correo electrónico único del usuario
        password_hash: Hash de la contraseña (nunca se almacena la contraseña en texto plano)
        nombre: Nombre completo del usuario
        fecha_creacion: Fecha y hora de creación del registro
        activo: Indica si el usuario está activo en el sistema
    """

    # Campos de la tabla
    id: Optional[int] = Field(
        default=None, primary_key=True, description="Identificador único del usuario"
    )

    username: str = Field(
        max_length=50, unique=True, index=True, description="Nombre de usuario único"
    )

    email: str = Field(
        max_length=255, unique=True, index=True, description="Correo electrónico único"
    )

    password_hash: str = Field(
        max_length=255, description="Hash de la contraseña almacenada"
    )

    nombre: str = Field(max_length=100, description="Nombre completo del usuario")

    fecha_creacion: datetime = Field(
        default_factory=datetime.now, description="Fecha de creación del usuario"
    )

    activo: bool = Field(default=True, description="Indica si el usuario está activo")

    def __repr__(self) -> str:
        """Representación legible del usuario."""
        return f"<Usuario(id={self.id}, username={self.username}, email={self.email})>"
