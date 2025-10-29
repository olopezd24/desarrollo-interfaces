import tkinter as tk

def actualizar(valor):
    lbl.config(text=f"Valor: {valor}")

root = tk.Tk()
root.title("Ejercicio 11 - Scale")

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar)
scale.pack(pady=8)

lbl = tk.Label(root, text="Valor: 0")
lbl.pack(pady=8)

root.mainloop()
