import tkinter as tk

def mostrar():
    sel = lb.curselection()
    if sel:
        fruta = lb.get(sel[0])
        lbl.config(text=f"Seleccionaste: {fruta}")

root = tk.Tk()
root.title("Ejercicio 6 - Listbox")

lb = tk.Listbox(root, height=5)
for fruta in ("Manzana", "Banana", "Naranja"):
    lb.insert(tk.END, fruta)
lb.pack(pady=5)

btn = tk.Button(root, text="Mostrar selección", command=mostrar)
btn.pack(pady=5)

lbl = tk.Label(root, text="")
lbl.pack(pady=5)

root.mainloop()
