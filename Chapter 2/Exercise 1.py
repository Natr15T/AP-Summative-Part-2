import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Welcome App")

# Set default window size
root.geometry("400x200")

# Disable resizing
root.resizable(False, False)

# Set background color
root.configure(bg="#AED6F1")  # Light blue

# Create welcome label with custom font
welcome_label = tk.Label(
    root,
    text="Welcome to the Application!",
    font=("Arial", 16, "bold"),  # Font name, size, bold
    bg="#AED6F1",  # Match background color
    fg="darkblue"  # Text color
)
welcome_label.pack(expand=True)

# Start the GUI loop
root.mainloop()
