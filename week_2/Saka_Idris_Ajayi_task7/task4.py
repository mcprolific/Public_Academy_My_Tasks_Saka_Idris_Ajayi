print("Task4: Unique Members Registration \n")
# Ask the user to enter three names separated by commas.
names_input = input("Enter three names separated by commas: ")

#    Convert them to a set to ensure uniqueness.
set_of_names = set(names_input.split(","))

#    Create a dictionary where each name is a key and its length is the value.
name_dict = {name.strip(): len(name.strip()) for name in set_of_names}

# Print the dictionary
print("\n===== Unique Members Registration =====")
print(name_dict)

# Requirements:

#    Use `.split(",")` and `set()` to remove duplicates.

#    Use dictionary comprehension `{name: len(name) for name in set_of_names}`.