import tkinter as tk
from tkinter import messagebox

usuarios = []

def anadir():
    nombre = ent_nombre.get()
    edad = escala_edad.get()
    genero = var_genero.get()
    if nombre:
        usuarios.append((nombre, edad, genero))
        lista.insert(tk.END, f"{nombre} - {edad} - {genero}")

def eliminar():
    sel = lista.curselection()
    if sel:
        lista.delete(sel[0])

def guardar_lista():
    messagebox.showinfo("Guardar Lista", "Guardado (mensaje de ejemplo)")

def cargar_lista():
    messagebox.showinfo("Cargar Lista", "Cargado (mensaje de ejemplo)")

def salir():
    root.quit()

root = tk.Tk()
root.title("Ejercicio 12 - Registro de Usuarios")

tk.Label(root, text="Nombre:").grid(row=0, column=0, sticky="w", padx=4, pady=4)
ent_nombre = tk.Entry(root, width=30)
ent_nombre.grid(row=0, column=1, padx=4, pady=4)

tk.Label(root, text="Edad:").grid(row=1, column=0, sticky="w", padx=4, pady=4)
escala_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
escala_edad.grid(row=1, column=1, padx=4, pady=4, sticky="we")

tk.Label(root, text="Género:").grid(row=2, column=0, sticky="w", padx=4, pady=4)
var_genero = tk.StringVar(value="otro")
tk.Radiobutton(root, text="Masculino", variable=var_genero, value="masculino").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Femenino",  variable=var_genero, value="femenino").grid(row=3, column=1, sticky="w")
tk.Radiobutton(root, text="Otro",      variable=var_genero, value="otro").grid(row=4, column=1, sticky="w")

tk.Button(root, text="Añadir", command=anadir).grid(row=5, column=0, padx=4, pady=4)
tk.Button(root, text="Eliminar", command=eliminar).grid(row=5, column=1, padx=4, pady=4, sticky="w")
tk.Button(root, text="Salir", command=salir).grid(row=5, column=1, padx=4, pady=4, sticky="e")

lista = tk.Listbox(root, height=8)
lista.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=4, pady=4)
scroll = tk.Scrollbar(root, orient="vertical", command=lista.yview)
scroll.grid(row=6, column=2, sticky="ns")
lista.config(yscrollcommand=scroll.set)

menubar = tk.Menu(root)
m_archivo = tk.Menu(menubar, tearoff=0)
m_archivo.add_command(label="Guardar Lista", command=guardar_lista)
m_archivo.add_command(label="Cargar Lista", command=cargar_lista)
menubar.add_cascade(label="Archivo", menu=m_archivo)
root.config(menu=menubar)

root.mainloop()
