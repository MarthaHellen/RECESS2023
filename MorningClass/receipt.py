import tkinter as tk
from tkinter import messagebox

class ReceiptGenerator:
    def __init__(self, window):
        self.window = window
        self.window.title("Martha's Receipt Generator")
        window.configure (bg="#17161b")
        
        self.item_name = tk.StringVar()
        self.item_quantity = tk.IntVar()
        self.item_price = tk.DoubleVar()
        
        self.item_name_label = tk.Label(window, text="Item Name:", bg="#17161b", fg="white", font=("Courier", 20))
        self.item_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.item_name_entry = tk.Entry(window, textvariable=self.item_name)
        self.item_name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.item_quantity_label = tk.Label(window, text="Quantity:", bg="#17161b", fg="white", font=("Courier", 20))
        self.item_quantity_label.grid(row=1, column=0, padx=10, pady=10)
        self.item_quantity_entry = tk.Entry(window, textvariable=self.item_quantity)
        self.item_quantity_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.item_price_label = tk.Label(window, text="Price:", bg="#17161b", fg="white", font=("Courier", 20))
        self.item_price_label.grid(row=2, column=0, padx=10, pady=10)
        self.item_price_entry = tk.Entry(window, textvariable=self.item_price)
        self.item_price_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.add_button = tk.Button(window, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        self.receipt_text = tk.Text(window, height=10, width=30)
        self.receipt_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        self.total_label = tk.Label(window, text="Total:")
        self.total_label.grid(row=5, column=0, padx=10, pady=10)
        self.total_value = tk.Label(window, text="")
        self.total_value.grid(row=5, column=1, padx=10, pady=10)
        
        self.items = []
        
    def add_item(self):
        name = self.item_name.get()
        quantity = self.item_quantity.get()
        price = self.item_price.get()
        
        if name and quantity and price:
            item_total = quantity * price
            self.items.append((name, quantity, price, item_total))
            self.update_receipt()
            self.clear_inputs()
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")
    
    def update_receipt(self):
        self.receipt_text.delete("1.0", tk.END)
        
        total = 0
        
        for item in self.items:
            name, quantity, price, item_total = item
            self.receipt_text.insert(tk.END, f"{name} -> {quantity} = UGX {item_total:.2f}\n")
            total += item_total
        
        self.total_value.config(text=f"UGX {total:.2f}")
    
    def clear_inputs(self):
        self.item_name.set("")
        self.item_quantity.set(0)
        self.item_price.set(0.0)
    
window = tk.Tk()
receipt_generator = ReceiptGenerator(window)
window.mainloop()