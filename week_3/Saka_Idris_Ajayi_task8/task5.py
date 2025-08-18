print("Task5: Store Inventory Update \n")
# Create a dictionary called store with items and their available quantities. Example:
# store = {"Book": 10, "Pen": 20, "Bag": 5}

store = {"Book": 10, "Pen": 20, "Bag": 5}
print("Before purchase:", store)

# Ask the user to input the item they want to buy (e.g., "Pen").
item = input("Enter the item you want to buy (Book/Pen/Bag): ")

# Ask the user to input the quantity they want to purchase.
quantity = int(input("Enter the quantity: "))

# Use the assignment operator -= to update (reduce) the item quantity in the dictionary.
if item in store:
    if quantity <= store[item]:
        store[item] -= quantity   # Use -= to reduce quantity
    else:
        print(f"Sorry, only {store[item]} {item}(s) available.")
else:
    print("Item not found in store.")


# Print the updated dictionary in this format:
print("After purchase:", store)



# Before purchase: {'Book': 10, 'Pen': 20, 'Bag': 5}
# After purchase: {'Book': 10, 'Pen': 18, 'Bag': 5}
