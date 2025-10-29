import tkinter as tk
from tkinter import messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 14 - Registro (clases)")

        tk.Label(root, text="Nombre:").grid(row=0, column=0, sticky="w", padx=4, pady=4)
        self.ent_nombre = tk.Entry(root, width=30)
        self.ent_nombre.grid(row=0, column=1, padx=4, pady=4)

        tk.Label(root, text="Edad:").grid(row=1, column=0, sticky="w", padx=4, pady=4)
        self.escala_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
        self.escala_edad.grid(row=1, column=1, padx=4, pady=4, sticky="we")

        tk.Label(root, text="Género:").grid(row=2, column=0, sticky="w", padx=4, pady=4)
        self.var_genero = tk.StringVar(value="otro")
        tk.Radiobutton(root, text="Masculino", variable=self.var_genero, value="masculino").grid(row=2, column=1, sticky="w")
        tk.Radiobutton(root, text="Femenino",  variable=self.var_genero, value="femenino").grid(row=3, column=1, sticky="w")
        tk.Radiobutton(root, text="Otro",      variable=self.var_genero, value="otro").grid(row=4, column=1, sticky="w")

        tk.Button(root, text="Añadir", command=self.anadir_usuario).grid(row=5, column=0, padx=4, pady=4)
        tk.Button(root, text="Eliminar", command=self.eliminar_usuario).grid(row=5, column=1, padx=4, pady=4, sticky="w")
        tk.Button(root, text="Salir", command=self.salir).grid(row=5, column=1, padx=4, pady=4, sticky="e")

        self.lista = tk.Listbox(root, height=8)
        self.lista.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=4, pady=4)
        self.scroll = tk.Scrollbar(root, orient="vertical", command=self.lista.yview)
        self.scroll.grid(row=6, column=2, sticky="ns")
        self.lista.config(yscrollcommand=self.scroll.set)

        menubar = tk.Menu(root)
        m_archivo = tk.Menu(menubar, tearoff=0)
        m_archivo.add_command(label="Guardar Lista", command=lambda: messagebox.showinfo("Guardar Lista", "Guardado"))
        m_archivo.add_command(label="Cargar Lista", command=lambda: messagebox.showinfo("Cargar Lista", "Cargado"))
        menubar.add_cascade(label="Archivo", menu=m_archivo)
        root.config(menu=menubar)

    def anadir_usuario(self):
        nombre = self.ent_nombre.get()
        edad = self.escala_edad.get()
        genero = self.var_genero.get()
        if nombre:
            self.lista.insert(tk.END, f"{nombre} - {edad} - {genero}")

    def eliminar_usuario(self):
        sel = self.lista.curselection()
        if sel:
            self.lista.delete(sel[0])

    def salir(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()
