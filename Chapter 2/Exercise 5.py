import tkinter as tk
from tkinter import messagebox

# Function to perform the selected operation
def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        return
    
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero is not allowed.")
            return
        result = num1 / num2
    elif operation == "Modulo":
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero is not allowed.")
            return
        result = num1 % num2
    else:
        result = "Unknown operation"
    
    result_var.set(f"Result: {result}")

# Main window
root = tk.Tk()
root.title("Basic Arithmetic Calculator")
root.geometry("400x250")

# Entry widgets for numbers
tk.Label(root, text="Number 1:").pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

tk.Label(root, text="Number 2:").pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Operation buttons
tk.Button(button_frame, text="Add", width=10, command=lambda: calculate("Add")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Subtract", width=10, command=lambda: calculate("Subtract")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Multiply", width=10, command=lambda: calculate("Multiply")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Divide", width=10, command=lambda: calculate("Divide")).grid(row=1, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Modulo", width=10, command=lambda: calculate("Modulo")).grid(row=2, column=0, columnspan=2, pady=5)

# Result label
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
