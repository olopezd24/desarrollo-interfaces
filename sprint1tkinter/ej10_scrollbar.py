import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 10 - Scrollbar")

texto = tk.Text(root, wrap="word", width=50, height=15)
texto.pack(side="left", fill="both", expand=True)

scroll = tk.Scrollbar(root, orient="vertical")
scroll.pack(side="right", fill="y")

scroll.config(command=texto.yview)
texto.config(yscrollcommand=scroll.set)

for i in range(1, 51):
    texto.insert(tk.END, f"Línea {i}: Ejemplo de texto largo.\n")

root.mainloop()
