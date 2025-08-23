# 2. Runtime Errors

# a. ZeroDivisionError – Dividing by zero.

# b. NameError – Using a variable before defining it.

# c. TypeError – Wrong data type in an operation.

# d. ValueError – Invalid value for a function.

# e. IndexError – Accessing list index out of range.

# f. KeyError – Accessing a dictionary with a missing key.

# g. FileNotFoundError – File does not exist.


# 2. Runtime Errors Demonstration

# a. ZeroDivisionError – Dividing by zero.
result = 10 / 0  # Program will stop here

# b. NameError – Using a variable before defining it.
print(undeclared_variable)

# c. TypeError – Wrong data type in an operation.
number = 5 + "hello"

# d. ValueError – Invalid value for a function.
num = int("abc")

# e. IndexError – Accessing list index out of range.
my_list = [1, 2, 3]
print(my_list[5])

# f. KeyError – Accessing a dictionary with a missing key.
my_dict = {"name": "Saka"}
print(my_dict["age"])

# g. FileNotFoundError – File does not exist.
with open("non_existent_file.txt", "r") as file:
    content = file.read()