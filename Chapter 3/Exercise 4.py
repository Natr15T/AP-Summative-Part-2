import tkinter as tk
from tkinter import StringVar, messagebox

# Function to draw the selected shape
def draw_shape():
    canvas.delete("all")  # Clear previous shapes
    shape = shape_var.get()
    
    try:
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integer coordinates.")
        return
    
    if shape == "Oval":
        canvas.create_oval(x1, y1, x2, y2, fill="blue")
    elif shape == "Square":
        # Ensure square by taking min width/height
        side = min(abs(x2 - x1), abs(y2 - y1))
        canvas.create_rectangle(x1, y1, x1 + side, y1 + side, fill="orange")
    elif shape == "Triangle":
        # Draw triangle using 3 points: bottom-left, bottom-right, top-middle
        points = [x1, y2, x2, y2, (x1 + x2)//2, y1]
        canvas.create_polygon(points, fill="red")
    else:
        messagebox.showerror("Error", "Please select a shape.")

# Main window
root = tk.Tk()
root.title("Shape Drawer")
root.geometry("600x500")

# Shape selection
shape_var = StringVar(value="Oval")
tk.Label(root, text="Select Shape:").pack(pady=5)
shapes = ["Oval", "Square", "Triangle"]  # Removed Rectangle
tk.OptionMenu(root, shape_var, *shapes).pack(pady=5)

# Coordinate inputs
coord_frame = tk.Frame(root)
coord_frame.pack(pady=10)

tk.Label(coord_frame, text="x1:").grid(row=0, column=0)
entry_x1 = tk.Entry(coord_frame, width=5)
entry_x1.grid(row=0, column=1)

tk.Label(coord_frame, text="y1:").grid(row=0, column=2)
entry_y1 = tk.Entry(coord_frame, width=5)
entry_y1.grid(row=0, column=3)

tk.Label(coord_frame, text="x2:").grid(row=1, column=0)
entry_x2 = tk.Entry(coord_frame, width=5)
entry_x2.grid(row=1, column=1)

tk.Label(coord_frame, text="y2:").grid(row=1, column=2)
entry_y2 = tk.Entry(coord_frame, width=5)
entry_y2.grid(row=1, column=3)

# Draw button
tk.Button(root, text="Draw Shape", command=draw_shape, bg="lightblue").pack(pady=10)

# Canvas for drawing
canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack(pady=10)

root.mainloop()
