print("Task4: Tuple Unpacking \n")
print("A. Ask a user for their; \n")

#   - First name
first_name = str(input("Enter your first name: "))

#   - Age
age = input("Enter your age: ")

#   - Favorite color
color = input("Enter your color: ")

#   - Home town
home_town = input("Enter your home town: ")

#   - Store them in a tuple profile and unpack into variables.
tuple_store = [first_name, age, color, home_town]

#   - Print and use  escape sequence to align each piece of information nicely.

print(f"My first name is {first_name}, my age is {age}, my favorite color is {color} and my home town is {home_town}.")
