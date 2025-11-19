import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView, AddUserView


class AppController:
    def __init__(self, master):
        self.master = master
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"
        self.avatar_images = {}

        self.modelo = GestorUsuarios()
        self.vista = MainView(master)

        self.refrescar_lista_usuarios()

    def refrescar_lista_usuarios(self):
        usuarios = self.modelo.listar()
        self.vista.actualizar_lista_usuarios(usuarios, self.seleccionar_usuario)

    def seleccionar_usuario(self, indice):
        usuario = self.modelo.listar()[indice]
        avatar_image = None
        if usuario.avatar:
            avatar_path = self.ASSETS_PATH / usuario.avatar
            if avatar_path.exists():
                if usuario.avatar not in self.avatar_images:
                    self.avatar_images[usuario.avatar] = tk.PhotoImage(file=str(avatar_path))
                avatar_image = self.avatar_images[usuario.avatar]
        self.vista.mostrar_detalles_usuario(usuario, avatar_image)

    def abrir_ventana_añadir(self):
        add_view = AddUserView(self.master)
        add_view.guardar_button.configure(command=lambda: self.añadir_usuario(add_view))

    def añadir_usuario(self, add_view):
        data = add_view.get_data()

        try:
            edad_int = int(data["edad"])
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return

        nuevo_usuario = Usuario(
            data["nombre"],
            edad_int,
            data["genero"],
            data["avatar"]
        )

        self.modelo.añadir_usuario(nuevo_usuario)
        self.refrescar_lista_usuarios()
        add_view.window.destroy()
