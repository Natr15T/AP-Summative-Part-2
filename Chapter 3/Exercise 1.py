import tkinter as tk
from tkinter import StringVar, OptionMenu

# Function to update the greeting
def update_greeting():
    name = name_var.get()
    color = color_var.get()
    greeting_label.config(text=f"Hello, {name}!", fg=color)

# Main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("400x250")

# InputFrame
input_frame = tk.Frame(root, bg="#D6EAF8", padx=10, pady=10)
input_frame.pack(fill="both", expand=True)

# Title label
title_label = tk.Label(input_frame, text="Enter Your Details", fg="blue", bg="#D6EAF8", font=("Arial", 14, "bold"))
title_label.pack(pady=5)

# Name entry
name_var = StringVar()
name_label = tk.Label(input_frame, text="Name:", bg="#D6EAF8")
name_label.pack(pady=2)
name_entry = tk.Entry(input_frame, textvariable=name_var)
name_entry.pack(pady=2)

# Color dropdown
color_var = StringVar(value="black")
color_label = tk.Label(input_frame, text="Select Color:", bg="#D6EAF8")
color_label.pack(pady=2)
colors = ["red", "green", "blue", "orange", "purple"]
color_dropdown = OptionMenu(input_frame, color_var, *colors)
color_dropdown.pack(pady=2)

# Update button
update_button = tk.Button(input_frame, text="Update Greeting", command=update_greeting)
update_button.pack(pady=5)

# DisplayFrame
display_frame = tk.Frame(root, bg="#FCF3CF", padx=10, pady=10)
display_frame.pack(fill="both", expand=True)

# Greeting label (initially empty)
greeting_label = tk.Label(display_frame, text="", bg="#FCF3CF", font=("Arial", 12))
greeting_label.pack(pady=20)

# Start the GUI loop
root.mainloop()
