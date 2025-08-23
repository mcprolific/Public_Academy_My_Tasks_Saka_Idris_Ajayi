# TASK: Build an Inventory Management System (Dictionary-Based)

# Requirements:
# Use a dictionary to store inventory items:
# inventory = {
#     "P001": {"name": "Laptop", "price": 350000, "quantity": 5},
#     "P002": {"name": "Mouse", "price": 5000, "quantity": 20}
# }

# Features to implement:
# Add New Product (auto-generate unique product IDs).
# View All Products (show in table format with total stock value = price × quantity).
# Search Product by ID.
# Update Product Details (name, price, quantity).
# Delete Product.
# Sell Product (reduce quantity, show total cost of sale).

# Ensure input validation (price and quantity must be positive).
# Keep the menu running until the user exits.


import random

# Initial Inventory Dictionary
inventory = {
    "P001": {"name": "Laptop", "price": 350000, "quantity": 5},
    "P002": {"name": "Mouse", "price": 5000, "quantity": 20}
}

# Function to auto-generate product ID
def generate_product_id():
    return "P" + str(random.randint(100, 999))

# Add New Product
def add_product():
    name = input("Enter product name: ").capitalize()
    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        if price <= 0 or quantity <= 0:
            print("Price and quantity must be positive!")
            return
        product_id = generate_product_id()
        inventory[product_id] = {"name": name, "price": price, "quantity": quantity}
        print(f"Product added successfully with ID: {product_id}")
    except ValueError:
        print("Invalid input! Price and quantity must be numbers.")

# View All Products
def view_products():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nID\tName\t\tPrice\t\tQuantity\tTotal Value")
    print("-" * 60)
    for pid, details in inventory.items():
        total_value = details["price"] * details["quantity"]
        print(f"{pid}\t{details['name']}\t{details['price']}\t{details['quantity']}\t{total_value}")
    print("-" * 60)

# Search Product by ID
def search_product():
    pid = input("Enter Product ID: ").upper()
    if pid in inventory:
        print(f"Product Found: {inventory[pid]}")
    else:
        print("Product not found!")

# Update Product
def update_product():
    pid = input("Enter Product ID to update: ").upper()
    if pid in inventory:
        print("Leave blank to keep current value.")
        name = input("Enter new name: ").capitalize() or inventory[pid]["name"]
        try:
            price = input("Enter new price: ")
            quantity = input("Enter new quantity: ")
            price = float(price) if price else inventory[pid]["price"]
            quantity = int(quantity) if quantity else inventory[pid]["quantity"]
            if price <= 0 or quantity <= 0:
                print("Price and quantity must be positive!")
                return
            inventory[pid] = {"name": name, "price": price, "quantity": quantity}
            print("Product updated successfully!")
        except ValueError:
            print("Invalid input!")
    else:
        print("Product ID not found!")

# Delete Product
def delete_product():
    pid = input("Enter Product ID to delete: ").upper()
    if pid in inventory:
        del inventory[pid]
        print("Product deleted successfully!")
    else:
        print("Product not found!")

# Sell Product
def sell_product():
    pid = input("Enter Product ID to sell: ").upper()
    if pid in inventory:
        try:
            qty = int(input("Enter quantity to sell: "))
            if qty <= 0:
                print("Quantity must be positive!")
                return
            if inventory[pid]["quantity"] >= qty:
                total_cost = inventory[pid]["price"] * qty
                inventory[pid]["quantity"] -= qty
                print(f"Sold {qty} units of {inventory[pid]['name']} for ₦{total_cost}")
            else:
                print("Insufficient stock!")
        except ValueError:
            print("Invalid quantity!")
    else:
        print("Product ID not found!")

# Main Menu
def main_menu():
    while True:
        print("\n--- INVENTORY MANAGEMENT SYSTEM ---")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Sell Product")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            sell_product()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

main_menu()
