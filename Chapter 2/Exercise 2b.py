import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Frames and Labels Pack Demo")
root.geometry("500x300")  # Default window size

# Left Frame
left_frame = tk.Frame(root, bd=5, relief="groove", bg="#AED6F1")
left_frame.pack(side="left", fill="both", expand=1, padx=5, pady=5)

# Right Frame
right_frame = tk.Frame(root, bd=5, relief="groove", bg="#F9E79F")
right_frame.pack(side="right", fill="both", expand=1, padx=5, pady=5)

# Labels in left frame
label_a = tk.Label(left_frame, text="Label A", bg="black", fg="white")
label_a.pack(side="top", fill="both", expand=1, padx=5, pady=5)

label_b = tk.Label(left_frame, text="Label B", bg="grey", fg="white")
label_b.pack(side="bottom", fill="both", expand=1, padx=5, pady=5)

# Labels in right frame
label_c = tk.Label(right_frame, text="Label C", bg="grey", fg="white")
label_c.pack(side="top", fill="both", expand=1, padx=5, pady=5)

label_d = tk.Label(right_frame, text="Label D", bg="black", fg="white")
label_d.pack(side="bottom", fill="both", expand=1, padx=5, pady=5)

# Start the GUI loop
root.mainloop()

