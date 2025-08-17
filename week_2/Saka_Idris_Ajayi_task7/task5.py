print("Task5: Contact Quick Lookup \n")
# Store three names and their phone numbers in two separate tuples.
names = ("Saka", "Ayeminimowa", "Animashanu")
numbers = ("08133274250", "08121647744", "081179577243")


#   Create a dictionary from them using `dict(zip(...))`.
contacts = dict(zip(names, numbers))

#   Ask the user for a name.
name = input("Enter a name to look up: ")

# Display the corresponding number (or an error message)
print(contacts.get(name, "Name not found in contacts."))

# Requirements:

#   Use `zip()` and d`ict()` to combine tuples.

#   Use `.get()` for safe retrieval.

#   No loops.