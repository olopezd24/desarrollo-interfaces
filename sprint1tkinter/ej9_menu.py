import tkinter as tk
from tkinter import messagebox

def abrir():
    messagebox.showinfo("Abrir", "Has elegido Abrir")

root = tk.Tk()
root.title("Ejercicio 9 - Menu")

menubar = tk.Menu(root)

m_archivo = tk.Menu(menubar, tearoff=0)
m_archivo.add_command(label="Abrir", command=abrir)
m_archivo.add_separator()
m_archivo.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=m_archivo)

m_ayuda = tk.Menu(menubar, tearoff=0)
m_ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Ejemplo Tkinter"))
menubar.add_cascade(label="Ayuda", menu=m_ayuda)

root.config(menu=menubar)
root.mainloop()
