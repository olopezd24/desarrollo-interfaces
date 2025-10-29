import tkinter as tk

def aplicar_color():
    root.config(bg=var_color.get())

root = tk.Tk()
root.title("Ejercicio 5 - Radiobutton")

var_color = tk.StringVar(value="white")

tk.Radiobutton(root, text="Rojo",  variable=var_color, value="red",    command=aplicar_color).pack(anchor="w")
tk.Radiobutton(root, text="Verde", variable=var_color, value="green",  command=aplicar_color).pack(anchor="w")
tk.Radiobutton(root, text="Azul",  variable=var_color, value="blue",   command=aplicar_color).pack(anchor="w")

root.mainloop()
