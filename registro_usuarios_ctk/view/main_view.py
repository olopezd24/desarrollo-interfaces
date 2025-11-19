import customtkinter as ctk


class MainView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        master.title("Registro de usuarios")
        master.geometry("800x500")
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(self)
        self.lista_usuarios_scrollable.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.detalle_frame = ctk.CTkFrame(self)
        self.detalle_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.label_nombre = ctk.CTkLabel(self.detalle_frame, text="Nombre:")
        self.label_nombre_value = ctk.CTkLabel(self.detalle_frame, text="-")

        self.label_edad = ctk.CTkLabel(self.detalle_frame, text="Edad:")
        self.label_edad_value = ctk.CTkLabel(self.detalle_frame, text="-")

        self.label_genero = ctk.CTkLabel(self.detalle_frame, text="Género:")
        self.label_genero_value = ctk.CTkLabel(self.detalle_frame, text="-")

        self.label_avatar = ctk.CTkLabel(self.detalle_frame, text="Avatar:")
        self.label_avatar_value = ctk.CTkLabel(self.detalle_frame, text="-")

        self.avatar_label = ctk.CTkLabel(self.detalle_frame, text="")

        self.label_nombre.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.label_nombre_value.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        self.label_edad.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.label_edad_value.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        self.label_genero.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.label_genero_value.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        self.label_avatar.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.label_avatar_value.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        self.avatar_label.grid(row=4, column=0, columnspan=2, pady=10)

        for i in range(5):
            self.detalle_frame.grid_rowconfigure(i, weight=0)
        self.detalle_frame.grid_columnconfigure(0, weight=0)
        self.detalle_frame.grid_columnconfigure(1, weight=1)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        for widget in self.lista_usuarios_scrollable.winfo_children():
            widget.destroy()

        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=2)

    def mostrar_detalles_usuario(self, usuario, avatar_image=None):
        self.label_nombre_value.configure(text=usuario.nombre)
        self.label_edad_value.configure(text=str(usuario.edad))
        self.label_genero_value.configure(text=usuario.genero)
        self.label_avatar_value.configure(text=usuario.avatar)

        if avatar_image is not None:
            self.avatar_label.configure(image=avatar_image, text="")
            self.avatar_label.image = avatar_image
        else:
            self.avatar_label.configure(image="", text="")
            self.avatar_label.image = None

class AddUserView:
    def __init__(self, master):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("300x350")
        self.window.grab_set()

        self.nombre_entry = ctk.CTkEntry(self.window, placeholder_text="Nombre")
        self.nombre_entry.pack(padx=10, pady=10)

        self.edad_entry = ctk.CTkEntry(self.window, placeholder_text="Edad")
        self.edad_entry.pack(padx=10, pady=10)

        self.genero_entry = ctk.CTkEntry(self.window, placeholder_text="Género")
        self.genero_entry.pack(padx=10, pady=10)

        self.avatar_entry = ctk.CTkEntry(self.window, placeholder_text="Nombre de avatar")
        self.avatar_entry.pack(padx=10, pady=10)

        self.guardar_button = ctk.CTkButton(self.window, text="Guardar")
        self.guardar_button.pack(padx=10, pady=20)

    def get_data(self):
        return {
            "nombre": self.nombre_entry.get(),
            "edad": self.edad_entry.get(),
            "genero": self.genero_entry.get(),
            "avatar": self.avatar_entry.get()
        }