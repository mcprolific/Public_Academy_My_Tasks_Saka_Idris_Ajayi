#=====Mixing Data Types=====
#===========================

#Ask for user input
age = int(input("Enter your age: "))             # integer
height = float(input("Enter your height in meters: "))  # float
name = input("Enter your name: ")                 # string

# Print a sentence using f-string showing all details in one line, making sure you type-cast where necessary.

print(f"{name} is {age} years old and {height} meters tall.")
