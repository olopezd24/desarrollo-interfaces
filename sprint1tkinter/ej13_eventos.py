import tkinter as tk

def click(event):
    x, y = event.x, event.y
    r = 10
    canvas.create_oval(x-r, y-r, x+r, y+r)

def limpiar(event=None):
    canvas.delete("all")

root = tk.Tk()
root.title("Ejercicio 13 - Eventos")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

canvas.bind("<Button-1>", click)
root.bind("c", limpiar)

root.mainloop()
