# String Operations Practice Questions

# Task1

# 1. Write a program to take a string input from the user and display it in uppercase.
firstname = input("Enter your firstname: ")
lastname = input("Enter your lastname: ")
print("My firstname is", firstname.upper(), "and my lastname is", lastname.upper())


# 2. Given the string "python", print its first and last characters.
valname = "python"
# Example of Indexing Operation Strings
# print(valname[0])       # Output: p
# print(valname[-1])      # Output: n
valprint1 = valname[0]      # Output: p
valprint2 = valname[-1]     # Output: n

print(valprint1 + valprint2) #pn

#==============OR================
# Example of Slicing Operation Strings
print(valname[0::5])    # Output: pn




# 3. Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.
firstname = input("Enter your firstname: ")
print("Hello,", firstname + "! where " + firstname + " is the user's input" )
print("Hello! This is my name: ", firstname)


# 4. Write a program to count the number of characters in a string without using len().
valname = "Idris"
# print(len(valname))
print(sum(1 for _ in valname)) 


# 5. Given "Hello World", replace "World" with "Python".
message = "Hello World"
print(message.replace("World", "Python"))

message2 = "Take your career to the next level with our specialized training"
print(message2.replace("level","step"))