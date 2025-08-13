# Task1: Fruit collector
# - Ask the user to enter 5 favourite fruits. Store them in a set and display the set.

fruit_store = set()

for i in range(5):
    fruit = input(f"Enter favourite fruit {i+1}: ")
    fruit_store.add(fruit)

# Display the set
print("\nYour favourite fruits are:", fruit_store)