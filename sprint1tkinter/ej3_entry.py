import tkinter as tk

def saludar():
    nombre = entrada.get()
    lbl.config(text=f"Hola, {nombre}")

root = tk.Tk()
root.title("Ejercicio 3 - Entry")

tk.Label(root, text="Escribe tu nombre:").pack(pady=5)
entrada = tk.Entry(root, width=30)
entrada.pack(pady=5)

btn = tk.Button(root, text="Saludar", command=saludar)
btn.pack(pady=5)

lbl = tk.Label(root, text="")
lbl.pack(pady=5)

root.mainloop()
