print("Task3: Online Store Cart Calculation \n")

# Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).

items = ["Book", "Pen", "Bag"]
prices = [500, 100, 2000]

# Start with an empty cart total (cart_total = 0).
cart_total = 0

# Use assignment operators (+=) to add the price of some items into cart_total.

cart_total += prices[0]   # Adding Book (500)
cart_total += prices[1]   # Adding Pen (100)

# Print the list of items and the total price using an f-string like this:

print(f"Items: {items}")
print(f"Total Price: ₦{cart_total}")


# Items: ['Book', 'Pen', 'Bag']
# Total Price: ₦600

