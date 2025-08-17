print("Task2: Super Market Price List")
print("A. Create a program that stores items and their prices in a dictionary. \n")
items = ["Garri", "Water", "Epa", "Sugar", "Milk"]

#   Items should come from a list.
price_list = {}
#   Prices are entered by the user.
print("Enter the prices for the following items:")

price_list["Garri"] = input(f"Price of {items[0]}: ")
price_list["Water"] = input(f"Price of {items[1]}: ")
price_list["Epa"] = input(f"Price of {items[2]}: ")
price_list["Sugar"] = input(f"Price of {items[3]}: ")
price_list["Milk"] = input(f"Price of {items[4]}: ")


#   Display all items and prices, then allow the user to update the price of an item.
print("\nSuper Market Price List:")
for food, price in price_list.items():
    print(f"{food}: N{price}")

print("Allow the user to update the price of an item \n")
food_to_update = input("Enter the name of the item you want to update: ")

if food_to_update in price_list:
    new_price = input(f"Enter the new price for {food_to_update}: ")
    if new_price.isdigit():
        # Use this ine to UPDATE my price
        price_list.update({food_to_update: float(new_price)})
        print(f"Updated {food_to_update} price to N{new_price}")
    else:
        print("Invalid input. Price not updated.")
else:
    print("Item not found in the list.")

# Display final updated price list
print("\n--- Updated Super Market Price List ---")
for food, price in price_list.items():
    print(f"{food}: N{price}")


# Requirements:

#   Use dictionary update method `.update()` or assignment.

#   Use `.keys()` to display available items.

#   Use input validation (no advanced functions).