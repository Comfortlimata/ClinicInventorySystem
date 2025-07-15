import tkinter as tk
from tkinter import messagebox, ttk
from logic.inventory_manager import add_medicine, get_all_medicines

def submit():
    name = name_entry.get()
    qty = quantity_entry.get()
    expiry = expiry_entry.get()
    if name and qty and expiry:
        add_medicine(name, int(qty), expiry)
        messagebox.showinfo("Success", "Medicine added successfully.")
        name_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        expiry_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "All fields are required.")

def display_inventory():
    def filter_inventory(*args):
        search_term = search_var.get().lower()
        for row in tree.get_children():
            tree.delete(row)
        for med in medicines:
            if search_term in str(med[1]).lower():  # Assuming med[1] is the name
                tree.insert('', 'end', values=med)

    medicines = get_all_medicines()
    inv_window = tk.Toplevel(root)
    inv_window.title("Inventory")
    inv_window.geometry("700x400")

    # Search bar
    search_var = tk.StringVar()
    search_var.trace_add('write', filter_inventory)
    tk.Label(inv_window, text="Search by Name:").pack(pady=5)
    tk.Entry(inv_window, textvariable=search_var, width=40).pack(pady=5)

    # Table/Grid using Treeview
    columns = ("ID", "Name", "Category", "Quantity", "Unit", "Expiry Date", "Date Added")
    tree = ttk.Treeview(inv_window, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(expand=True, fill='both', padx=10, pady=10)

    for med in medicines:
        tree.insert('', 'end', values=med)

root = tk.Tk()
root.title("Clinic Inventory")

tk.Label(root, text="Medicine Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Label(root, text="Expiry Date (YYYY-MM-DD)").pack()
expiry_entry = tk.Entry(root)
expiry_entry.pack()

tk.Button(root, text="Add", command=submit).pack(pady=5)
tk.Button(root, text="View Inventory", command=display_inventory).pack()

root.mainloop()
