import tkinter as tk
from tkinter import ttk, messagebox
import math

# Functions to calculate areas
def calculate_circle_area():
    try:
        radius = float(circle_radius.get())
        area = math.pi * radius ** 2
        circle_result.config(text=f"Area of Circle: {area:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid radius.")

def calculate_square_area():
    try:
        side = float(square_side.get())
        area = side ** 2
        square_result.config(text=f"Area of Square: {area:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid side length.")

def calculate_rectangle_area():
    try:
        length = float(rect_length.get())
        width = float(rect_width.get())
        area = length * width
        rectangle_result.config(text=f"Area of Rectangle: {area:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid dimensions.")

# Main window
root = tk.Tk()
root.title("Shape Area Calculator")
root.geometry("400x300")

# Tabbed interface
tab_control = ttk.Notebook(root)

# Circle tab
circle_tab = ttk.Frame(tab_control)
tab_control.add(circle_tab, text="Circle")
tk.Label(circle_tab, text="Radius:").pack(pady=5)
circle_radius = tk.StringVar()
tk.Entry(circle_tab, textvariable=circle_radius).pack(pady=5)
tk.Button(circle_tab, text="Calculate Area", command=calculate_circle_area).pack(pady=5)
circle_result = tk.Label(circle_tab, text="")
circle_result.pack(pady=5)

# Square tab
square_tab = ttk.Frame(tab_control)
tab_control.add(square_tab, text="Square")
tk.Label(square_tab, text="Side Length:").pack(pady=5)
square_side = tk.StringVar()
tk.Entry(square_tab, textvariable=square_side).pack(pady=5)
tk.Button(square_tab, text="Calculate Area", command=calculate_square_area).pack(pady=5)
square_result = tk.Label(square_tab, text="")
square_result.pack(pady=5)

# Rectangle tab
rectangle_tab = ttk.Frame(tab_control)
tab_control.add(rectangle_tab, text="Rectangle")
tk.Label(rectangle_tab, text="Length:").pack(pady=5)
rect_length = tk.StringVar()
tk.Entry(rectangle_tab, textvariable=rect_length).pack(pady=5)
tk.Label(rectangle_tab, text="Width:").pack(pady=5)
rect_width = tk.StringVar()
tk.Entry(rectangle_tab, textvariable=rect_width).pack(pady=5)
tk.Button(rectangle_tab, text="Calculate Area", command=calculate_rectangle_area).pack(pady=5)
rectangle_result = tk.Label(rectangle_tab, text="")
rectangle_result.pack(pady=5)

# Pack the tabs
tab_control.pack(expand=1, fill="both")

root.mainloop()
