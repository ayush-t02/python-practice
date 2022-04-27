import tkinter as tk
from tkinter import *

app = tk.Tk()
app.title("Canvas")
canvas = Canvas(app)
canvas.pack()
canvas.create_oval(10, 10, 80, 80,
                   outline="black", fill="white",
                   width=2)

# Creates an ellipse with horizontal diameter
# of 210 and vertical diameter of 80
canvas.create_oval(110, 10, 210, 80,
                   outline="red", fill="green",
                   width=2)

# Creates a rectangle of 50x60 (heightxwidth)
canvas.create_rectangle(230, 10, 290, 60,
                        outline="black", fill="blue",
                        width=2)

canvas.create_arc(30, 200, 90, 100, start=0,
                  extent=210, outline="green",
                  fill="red", width=2)
points = [150, 100, 200, 120, 240, 180,
          210, 200, 150, 150, 100, 200]
canvas.create_polygon(points, outline="blue",
                      fill="orange", width=2)

line = canvas.create_line(160, 230, 280, 250, fill='blue', width=5)

app.mainloop()
