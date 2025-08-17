# Task1: Fruit collector
# - Ask the user to enter 5 favourite fruits. Store them in a set and display the set.

fruit_store = set()

# Loop 5 times to collect fruit names from the user
for McP in range(5): #  Ask the user 
    fruit = input(f"Enter favourite fruit {McP+1}: ")
    fruit_store.add(fruit)

# Display the set
print("\nYour favourite fruits are:", fruit_store)