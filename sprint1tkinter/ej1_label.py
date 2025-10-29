import tkinter as tk

def cambiar():
    lbl3.config(text="Texto cambiado")

root = tk.Tk()
root.title("Ejercicio 1 - Label")

lbl1 = tk.Label(root, text="Bienvenido a Tkinter")
lbl1.pack(pady=5)

lbl2 = tk.Label(root, text="Óscar López de la Iglesia")
lbl2.pack(pady=5)

lbl3 = tk.Label(root, text="Texto inicial")
lbl3.pack(pady=5)

btn = tk.Button(root, text="Cambiar texto", command=cambiar)
btn.pack(pady=5)

root.mainloop()
