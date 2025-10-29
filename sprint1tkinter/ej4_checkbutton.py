import tkinter as tk

def actualizar():
    seleccionadas = []
    if var_leer.get() == 1: seleccionadas.append("Leer")
    if var_deporte.get() == 1: seleccionadas.append("Deporte")
    if var_musica.get() == 1: seleccionadas.append("Música")
    lbl.config(text=", ".join(seleccionadas))

root = tk.Tk()
root.title("Ejercicio 4 - Checkbutton")

var_leer = tk.IntVar(value=0)
var_deporte = tk.IntVar(value=0)
var_musica = tk.IntVar(value=0)

tk.Checkbutton(root, text="Leer", variable=var_leer, command=actualizar).pack(anchor="w")
tk.Checkbutton(root, text="Deporte", variable=var_deporte, command=actualizar).pack(anchor="w")
tk.Checkbutton(root, text="Música", variable=var_musica, command=actualizar).pack(anchor="w")

lbl = tk.Label(root, text="")
lbl.pack(pady=8, anchor="w")

root.mainloop()
