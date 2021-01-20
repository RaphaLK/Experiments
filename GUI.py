import tkinter as tk
from math import pi, radians


def buttonPress():
    """Prints 3 times when button is pressed"""
    for i in range (3):
        print("Button Works!~")

class ball:
    def __init__(circle):
        circle.radius = 2
        circle.colour = "Red"

root = tk.Tk()
root.title("Test GUI")

canvas = tk.Canvas(root, width = 700, height = 700, bg = "black")
canvas.pack()

frame = tk.Frame(canvas, bg =  "gray")
frame.place(relheight = 0.9, relwidth = 0.9, relx = 0.05, rely = 0.05)

button = tk.Button(root, width = 5, height = 1, bg = "cyan", 
                text = "Print", command = buttonPress)
button.pack()

label = tk.Label(frame, height = 200, width = 400, text = "Click the Button.", font = "arial 20")
label.pack()


root.mainloop()
