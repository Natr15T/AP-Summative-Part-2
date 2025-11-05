import tkinter as tk
from tkinter import ttk, messagebox

# --- Window setup ---
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x600")
root.config(bg="#f5f7fa")

# --- Header section ---
header_frame = tk.Frame(root, bg="#0a1128", height=80)
header_frame.pack(fill="x")

tk.Label(
    header_frame,
    text="BATH SPA\nUNIVERSITY",
    bg="#0a1128",
    fg="white",
    font=("Arial", 10, "bold"),
    justify="center"
).place(x=40, y=15)

tk.Label(
    header_frame,
    text="RAK\nCAMPUS",
    bg="#0a1128",
    fg="white",
    font=("Arial", 12, "bold"),
    justify="center"
).place(x=150, y=20)

# --- Title ---
title = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 13, "bold"),
    bg="#f5f7fa",
    fg="#111"
)
title.pack(pady=(15, 0))

subtitle = tk.Label(
    root,
    text="New Student Registration",
    font=("Arial", 10, "italic"),
    bg="#f5f7fa"
)
subtitle.pack(pady=(0, 10))

# --- Form frame ---
form = tk.Frame(root, bg="#f5f7fa")
form.pack(pady=5)

def make_label(text, row):
    tk.Label(form, text=text, bg="#f5f7fa", anchor="w").grid(row=row, column=0, sticky="w", pady=4, padx=10)

def make_entry(row):
    entry = tk.Entry(form, width=35, bg="#d3d3d3")
    entry.grid(row=row, column=1, pady=4)
    return entry

# Student info fields
make_label("Student Name", 0)
entry_name = make_entry(0)

make_label("Mobile Number", 1)
entry_mobile = make_entry(1)

make_label("Email Id", 2)
entry_email = make_entry(2)

make_label("Home Address", 3)
entry_address = make_entry(3)

# Gender
make_label("Gender", 4)
gender_cb = ttk.Combobox(form, values=["Male", "Female", "Other"], width=32)
gender_cb.grid(row=4, column=1, pady=4)

# Course
make_label("Course Enrolled", 5)
course_frame = tk.Frame(form, bg="#f5f7fa")
course_frame.grid(row=5, column=1, sticky="w")

course_var = tk.StringVar()
courses = ["BSc CC", "BSc CY", "BSc PSY", "BA & BM"]
for c in courses:
    tk.Radiobutton(course_frame, text=c, variable=course_var, value=c, bg="#f5f7fa").pack(anchor="w")

# Languages
make_label("Languages known", 6)
lang_frame = tk.Frame(form, bg="#f5f7fa")
lang_frame.grid(row=6, column=1, sticky="w")

lang_vars = {
    "English": tk.BooleanVar(),
    "Tagalog": tk.BooleanVar(),
    "Hindi/Urdu": tk.BooleanVar()
}
for lang, var in lang_vars.items():
    tk.Checkbutton(lang_frame, text=lang, variable=var, bg="#f5f7fa").pack(anchor="w")

# English skill slider
make_label("Rate your English communication skills", 7)
scale = tk.Scale(form, from_=0, to=10, orient="horizontal", length=200, bg="#f5f7fa")
scale.grid(row=7, column=1, sticky="w", pady=5)

# --- Button functions ---
def submit_form():
    messagebox.showinfo("Submitted", "Form submitted successfully!")

def clear_form():
    entry_name.delete(0, tk.END)
    entry_mobile.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    gender_cb.set('')
    course_var.set('')
    for var in lang_vars.values():
        var.set(False)
    scale.set(0)

# --- Buttons ---
btn_frame = tk.Frame(root, bg="#f5f7fa")
btn_frame.pack(pady=20)

submit_btn = tk.Button(btn_frame, text="Submit", bg="#0a1128", fg="white", width=12, height=1, command=submit_form)
submit_btn.grid(row=0, column=0, padx=15)

clear_btn = tk.Button(btn_frame, text="Clear", bg="#0a1128", fg="white", width=12, height=1, command=clear_form)
clear_btn.grid(row=0, column=1, padx=15)

root.mainloop()
