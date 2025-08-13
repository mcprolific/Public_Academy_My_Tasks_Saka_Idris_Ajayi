print("Task2: Tuple and Input")
print("A. Ask the user for 5 best friends’ names.\n")
friend_1 = input("Enter your first best friend: ")
friend_2 = input("Enter your second best friend: ")
friend_3 = input("Enter your third best friend: ")
friend_4 = input("Enter your fourth best friend: ")
friend_5 = input("Enter your fifth best friend: ")


print("B. Store them in a tuple friends. \n")
friendStore = [friend_1, friend_2, friend_3, friend_4, friend_5]
print(friendStore)

print("C. Print the tuple in reverse order. \n")
friendStore.reverse()
print(friendStore)