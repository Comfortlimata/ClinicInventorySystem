import tkinter as tk
from tkinter import messagebox, ttk
from logic.inventory_manager import add_medicine, get_all_medicines

# Color scheme
BG_COLOR = "#f4f6fb"
TITLE_BG = "#3a7ca5"
TITLE_FG = "#ffffff"
LABEL_COLOR = "#2d4059"
ENTRY_BG = "#ffffff"
BUTTON_BG = "#3a7ca5"
BUTTON_FG = "#ffffff"
BUTTON_ACTIVE_BG = "#24496b"
TABLE_HEADER_BG = "#3a7ca5"
TABLE_HEADER_FG = "#ffffff"
TABLE_ROW_BG = "#eaf0fa"
TABLE_ALT_ROW_BG = "#f4f6fb"


def submit():
    name = name_entry.get()
    category = category_entry.get()
    qty = quantity_entry.get()
    unit = unit_entry.get()
    expiry = expiry_entry.get()
    if name and qty and expiry:
        add_medicine(name, category, int(qty), unit, expiry)
        messagebox.showinfo("Success", "Medicine added successfully.")
        name_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        unit_entry.delete(0, tk.END)
        expiry_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "All fields are required.")

def display_inventory():
    def filter_inventory(*args):
        search_term = search_var.get().lower()
        for row in tree.get_children():
            tree.delete(row)
        for i, med in enumerate(medicines):
            if search_term in str(med[1]).lower():
                tags = ('evenrow',) if i % 2 == 0 else ('oddrow',)
                tree.insert('', 'end', values=med, tags=tags)

    medicines = get_all_medicines()
    inv_window = tk.Toplevel(root)
    inv_window.title("Inventory")
    inv_window.geometry("800x450")
    inv_window.configure(bg=BG_COLOR)

    # Title
    tk.Label(inv_window, text="Inventory", font=("Arial", 18, "bold"), bg=TITLE_BG, fg=TITLE_FG, pady=10).pack(fill=tk.X)

    # Search bar
    search_var = tk.StringVar()
    search_var.trace_add('write', filter_inventory)
    search_frame = tk.Frame(inv_window, bg=BG_COLOR)
    search_frame.pack(pady=10)
    tk.Label(search_frame, text="Search by Name:", bg=BG_COLOR, fg=LABEL_COLOR, font=("Arial", 11)).pack(side=tk.LEFT, padx=(0, 8))
    tk.Entry(search_frame, textvariable=search_var, width=40, bg=ENTRY_BG).pack(side=tk.LEFT)

    # Table/Grid using Treeview
    columns = ("ID", "Name", "Category", "Quantity", "Unit", "Expiry Date", "Date Added")
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",
                    background=TABLE_ROW_BG,
                    fieldbackground=TABLE_ROW_BG,
                    foreground=LABEL_COLOR,
                    rowheight=28,
                    font=("Arial", 11))
    style.configure("Treeview.Heading",
                    background=TABLE_HEADER_BG,
                    foreground=TABLE_HEADER_FG,
                    font=("Arial", 12, "bold"))
    style.map("Treeview",
              background=[('selected', BUTTON_BG)])
    style.configure("evenrow", background=TABLE_ROW_BG)
    style.configure("oddrow", background=TABLE_ALT_ROW_BG)

    tree = ttk.Treeview(inv_window, columns=columns, show='headings', selectmode='browse')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=110, anchor=tk.CENTER)
    tree.pack(expand=True, fill='both', padx=20, pady=10)

    tree.tag_configure('evenrow', background=TABLE_ROW_BG)
    tree.tag_configure('oddrow', background=TABLE_ALT_ROW_BG)

    for i, med in enumerate(medicines):
        tags = ('evenrow',) if i % 2 == 0 else ('oddrow',)
        tree.insert('', 'end', values=med, tags=tags)

root = tk.Tk()
root.title("Clinic Inventory System")
root.geometry("420x520")
root.configure(bg=BG_COLOR)

# Title
header = tk.Label(root, text="Clinic Inventory System", font=("Arial", 18, "bold"), bg=TITLE_BG, fg=TITLE_FG, pady=12)
header.pack(fill=tk.X)

form_frame = tk.Frame(root, bg=BG_COLOR)
form_frame.pack(pady=18)

# Name
name_label = tk.Label(form_frame, text="Medicine Name*", bg=BG_COLOR, fg=LABEL_COLOR, font=("Arial", 11))
name_label.grid(row=0, column=0, sticky="w", pady=6, padx=8)
name_entry = tk.Entry(form_frame, width=32, bg=ENTRY_BG)
name_entry.grid(row=0, column=1, pady=6, padx=8)

# Category
category_label = tk.Label(form_frame, text="Category", bg=BG_COLOR, fg=LABEL_COLOR, font=("Arial", 11))
category_label.grid(row=1, column=0, sticky="w", pady=6, padx=8)
category_entry = tk.Entry(form_frame, width=32, bg=ENTRY_BG)
category_entry.grid(row=1, column=1, pady=6, padx=8)

# Quantity
quantity_label = tk.Label(form_frame, text="Quantity*", bg=BG_COLOR, fg=LABEL_COLOR, font=("Arial", 11))
quantity_label.grid(row=2, column=0, sticky="w", pady=6, padx=8)
quantity_entry = tk.Entry(form_frame, width=32, bg=ENTRY_BG)
quantity_entry.grid(row=2, column=1, pady=6, padx=8)

# Unit
unit_label = tk.Label(form_frame, text="Unit", bg=BG_COLOR, fg=LABEL_COLOR, font=("Arial", 11))
unit_label.grid(row=3, column=0, sticky="w", pady=6, padx=8)
unit_entry = tk.Entry(form_frame, width=32, bg=ENTRY_BG)
unit_entry.grid(row=3, column=1, pady=6, padx=8)

# Expiry Date
expiry_label = tk.Label(form_frame, text="Expiry Date (YYYY-MM-DD)*", bg=BG_COLOR, fg=LABEL_COLOR, font=("Arial", 11))
expiry_label.grid(row=4, column=0, sticky="w", pady=6, padx=8)
expiry_entry = tk.Entry(form_frame, width=32, bg=ENTRY_BG)
expiry_entry.grid(row=4, column=1, pady=6, padx=8)

# Buttons
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=18)

add_btn = tk.Button(button_frame, text="Add", command=submit, bg=BUTTON_BG, fg=BUTTON_FG, activebackground=BUTTON_ACTIVE_BG, font=("Arial", 12, "bold"), width=14, bd=0, pady=6)
add_btn.grid(row=0, column=0, padx=10)

view_btn = tk.Button(button_frame, text="View Inventory", command=display_inventory, bg=BUTTON_BG, fg=BUTTON_FG, activebackground=BUTTON_ACTIVE_BG, font=("Arial", 12, "bold"), width=14, bd=0, pady=6)
view_btn.grid(row=0, column=1, padx=10)

root.mainloop()
