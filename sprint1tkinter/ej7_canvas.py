import tkinter as tk

def dibujar():
    try:
        x1 = int(e_x1.get()); y1 = int(e_y1.get())
        x2 = int(e_x2.get()); y2 = int(e_y2.get())
        cx = int(e_cx.get()); cy = int(e_cy.get()); r = int(e_r.get())
    except ValueError:
        return
    c.delete("all")
    c.create_rectangle(x1, y1, x2, y2)
    c.create_oval(cx - r, cy - r, cx + r, cy + r)

root = tk.Tk()
root.title("Ejercicio 7 - Canvas")

tk.Label(root, text="x1").grid(row=0, column=0); e_x1 = tk.Entry(root, width=5); e_x1.grid(row=0, column=1)
tk.Label(root, text="y1").grid(row=0, column=2); e_y1 = tk.Entry(root, width=5); e_y1.grid(row=0, column=3)
tk.Label(root, text="x2").grid(row=0, column=4); e_x2 = tk.Entry(root, width=5); e_x2.grid(row=0, column=5)
tk.Label(root, text="y2").grid(row=0, column=6); e_y2 = tk.Entry(root, width=5); e_y2.grid(row=0, column=7)

tk.Label(root, text="cx").grid(row=1, column=0); e_cx = tk.Entry(root, width=5); e_cx.grid(row=1, column=1)
tk.Label(root, text="cy").grid(row=1, column=2); e_cy = tk.Entry(root, width=5); e_cy.grid(row=1, column=3)
tk.Label(root, text="r").grid(row=1, column=4);  e_r  = tk.Entry(root, width=5); e_r.grid(row=1, column=5)

tk.Button(root, text="Dibujar", command=dibujar).grid(row=1, column=7, padx=5)

c = tk.Canvas(root, width=300, height=200, bg="white")
c.grid(row=2, column=0, columnspan=8, pady=8)

root.mainloop()
