"""
Script para crear usuario de prueba.
"""

import bcrypt
from sqlmodel import select
import reflex as rx
from todo_app.models.usuario import Usuario


def crear_usuario_prueba():
    with rx.session() as session:
        usuario_existente = session.exec(
            select(Usuario).where(Usuario.username == "demo")
        ).first()

        if usuario_existente:
            print("El usuario 'demo' ya existe.")
            return

        password_hash = bcrypt.hashpw(
            "demo123".encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

        nuevo_usuario = Usuario(
            username="demo",
            email="demo@taskflow.com",
            password_hash=password_hash,
            nombre="Usuario Demo",
            activo=True,
        )
        session.add(nuevo_usuario)
        session.commit()
        print("Usuario de prueba creado exitosamente!")
        print("  Usuario: demo")
        print("  Contrasena: demo123")


if __name__ == "__main__":
    crear_usuario_prueba()
