print("TASK 2. Shopping List Manager \n")

print("A. Create an empty list. \n")
empty_list = []
print(empty_list) 


print("B. Ask the user to enter 3 shopping items (one by one). \n")

item1 = input("Enter first shopping item: ")
item2 = input("Enter second shopping item: ")
item3 = input("Enter third shopping item: ")

print("C. Add them to the list. \n")
print("Format: Using empty_list.append(name of item)")
empty_list.append(item1)
empty_list.append(item2)
empty_list.append(item3)

print("D. Display the list as a single string, separated by commas. \n")

print("Your shopping list: " + ", ".join(empty_list))


