"""
Paquete de estados de la aplicación.
"""

from .auth import AuthState
from .tareas import TaskState, TareasState

__all__ = ["AuthState", "TaskState", "TareasState"]
