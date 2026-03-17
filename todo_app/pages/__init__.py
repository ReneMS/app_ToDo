"""
Paquete de páginas de la aplicación.
"""

from .auth import login_page, register_page
from .dashboard import dashboard_page

__all__ = ["login_page", "register_page", "dashboard_page"]
