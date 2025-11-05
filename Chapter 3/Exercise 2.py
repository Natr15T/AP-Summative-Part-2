import tkinter as tk
from tkinter import messagebox, StringVar, IntVar, OptionMenu

# Prices for each coffee type
COFFEE_PRICES = {
    "Espresso": 50,
    "Cappuccino": 70,
    "Latte": 80,
    "Americano": 60
}

# Initialize total
total_price = 0
order_summary = []

# Function to add coffee to the order
def add_to_order():
    global total_price, order_summary
    coffee = coffee_var.get()
    sugar = "Yes" if sugar_var.get() else "No"
    milk = "Yes" if milk_var.get() else "No"
    price = COFFEE_PRICES[coffee]
    
    # Add to order list and total
    order_summary.append(f"{coffee} (Sugar: {sugar}, Milk: {milk}) - {price}")
    total_price += price
    
    # Update order display
    order_display.config(state="normal")
    order_display.delete(1.0, tk.END)
    order_display.insert(tk.END, "\n".join(order_summary) + f"\n\nTotal: {total_price}")
    order_display.config(state="disabled")
    
    # Reset options
    sugar_var.set(0)
    milk_var.set(0)

# Function to complete the order and handle money
def complete_order():
    global total_price, order_summary
    try:
        money_inserted = float(money_var.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount of money.")
        return
    
    if money_inserted < total_price:
        messagebox.showwarning("Insufficient Money", f"Total price is {total_price}. Please insert more money.")
    else:
        change = money_inserted - total_price
        messagebox.showinfo(
            "Order Completed",
            f"Your orders:\n" + "\n".join(order_summary) + f"\n\nTotal Price: {total_price}\nMoney Inserted: {money_inserted}\nChange: {change:.2f}\nEnjoy your drinks!"
        )
        # Reset order
        total_price = 0
        order_summary = []
        order_display.config(state="normal")
        order_display.delete(1.0, tk.END)
        order_display.config(state="disabled")
        money_var.set("")

# Main window
root = tk.Tk()
root.title("Coffee Vending Machine")
root.geometry("450x500")

# Coffee type selection
coffee_var = StringVar(value="Espresso")
tk.Label(root, text="Select Coffee Type:").pack(pady=10)
coffee_options = ["Espresso", "Cappuccino", "Latte", "Americano"]
coffee_dropdown = OptionMenu(root, coffee_var, *coffee_options)
coffee_dropdown.pack(pady=5)

# Sugar and milk options
sugar_var = IntVar()
milk_var = IntVar()
tk.Checkbutton(root, text="Sugar", variable=sugar_var).pack(pady=2)
tk.Checkbutton(root, text="Milk", variable=milk_var).pack(pady=2)

# Add to Order button
tk.Button(root, text="Add to Order", command=add_to_order, bg="brown", fg="white").pack(pady=10)

# Order summary display
tk.Label(root, text="Current Order:").pack()
order_display = tk.Text(root, height=10, width=50, state="disabled")
order_display.pack(pady=5)

# Money insertion
tk.Label(root, text="Insert Money:").pack(pady=10)
money_var = StringVar()
tk.Entry(root, textvariable=money_var).pack(pady=5)

# Complete Order button
tk.Button(root, text="Complete Order", command=complete_order, bg="green", fg="white").pack(pady=15)

root.mainloop()
