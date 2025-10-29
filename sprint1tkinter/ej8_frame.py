import tkinter as tk

def mostrar():
    lbl_result.config(text=entrada.get())

def borrar():
    entrada.delete(0, tk.END)
    lbl_result.config(text="")

root = tk.Tk()
root.title("Ejercicio 8 - Frame")

frame_sup = tk.Frame(root, bd=1, relief="sunken")
frame_sup.pack(fill="x", padx=5, pady=5)

tk.Label(frame_sup, text="Etiqueta 1").grid(row=0, column=0, padx=4, pady=4, sticky="w")
tk.Label(frame_sup, text="Etiqueta 2").grid(row=0, column=1, padx=4, pady=4, sticky="w")
entrada = tk.Entry(frame_sup, width=30)
entrada.grid(row=1, column=0, columnspan=2, padx=4, pady=4, sticky="we")

frame_inf = tk.Frame(root, bd=1, relief="sunken")
frame_inf.pack(fill="x", padx=5, pady=5)

tk.Button(frame_inf, text="Mostrar", command=mostrar).grid(row=0, column=0, padx=4, pady=4)
tk.Button(frame_inf, text="Borrar",  command=borrar).grid(row=0, column=1, padx=4, pady=4)

lbl_result = tk.Label(root, text="")
lbl_result.pack(pady=6)

root.mainloop()
