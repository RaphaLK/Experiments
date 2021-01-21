import tkinter as tk
import math as mat
from typing import Text

root = tk.Tk()
root.title("Crude OCR")



canvas = tk.Canvas(root, height = 800, width = 1280)
canvas.pack()

button = tk.Button(canvas, height = 1, width = 20, bg = "black", text = "Jason Jeremy")
button.pack(side = tk.BOTTOM)

label = tk.Label(canvas, height = 200, width = 400, text = "CRUDE OCR", font = "arial 40")
label.pack()

root.mainloop()