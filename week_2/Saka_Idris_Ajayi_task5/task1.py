print("Tuple Practice")
print("Task1:  Create and Display \n")
print("Ask the user to enter three favorite Nigerian dishes (one at a time). \n")
dish_1 = input("Enter your first favorite Nigerian dishes: ")
dish_2 = input("Enter your second favorite Nigerian dishes: ")
dish_3 = input("Enter your third favorite Nigerian dishes: ")

print("B. Store them in a tuple called dishes. \n")
dishes = (dish_1, dish_2, dish_3)
# print(dishes)

print("C. Print the tuple in a single line, separating items with commas. \n")
print(dishes)

print("D. Use the \"\\n\", escape sequence to print each dish on a new line. \n")
print(f"dish_1 \ndish_2 \ndish_3")