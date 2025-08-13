print("Task3: Tuple Operations")
print("A. Create a tuple of 5 Nigerian states entered by the user.")
state_1 = input("Enter your first best state: ")
state_2 = input("Enter your second best state: ")
state_3 = input("Enter your third best state: ")
state_4 = input("Enter your fourth best state: ")
state_5 = input("Enter your fifth best state: ")


print("B. Print the first state and last state.")
tuple_state = (state_1, state_2, state_3, state_4, state_5)

print(tuple_state[0])
print(tuple_state[-1])

print("C. Check if 'Lagos' is in the tuple and print 'Yes' or 'No'.")
if "Lagos" in tuple_state :
    print("Yes! Lagos is inside your state") 


print("D. Print the number of states entered.")

for state_index in tuple_state:
    print(state_index)

#     - (Hint: use the tuple membership)