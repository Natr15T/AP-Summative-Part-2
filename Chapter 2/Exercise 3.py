import tkinter as tk
from tkinter import messagebox

# Function to handle login
def login():
    username = username_var.get()
    password = password_var.get()
    
    # Example validation (replace with real authentication)
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Main window
root = tk.Tk()
root.title("Login Page")
root.geometry("350x200")
root.resizable(False, False)

# Username label and entry
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
username_var = tk.StringVar()
tk.Entry(root, textvariable=username_var).grid(row=0, column=1, padx=10, pady=10)

# Password label and entry
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, show="*").grid(row=1, column=1, padx=10, pady=10)

# Login button
tk.Button(root, text="Login", command=login, bg="blue", fg="white").grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
