print("Task1: Student Bio Data Storage \n")
print("A. Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary. \n") 
student_data = {}


student_data["name"] = input("Enter your name: ")
student_data["age"] = int(input("Enter your age: "))
student_data["gender"] = input("Enter your gender: ")

print(student_data)

print("Ask how many courses the student is taking")
num_courses = int(input("How many courses are you taking? "))

print("Courses should be stored as a list. \n")  
# Collect courses
courses = []
for McP in range(num_courses):
    course = input(f"Enter course {McP+1}: ")
    courses.append(course)

print(courses)
student_data["courses"] = courses
print(student_data)

# Display the bio-data neatly using escape sequences.
print("\n===== STUDENT BIO DATA =====")

print(f"Name:\t\t{student_data['name']}")
print(f"Age:\t\t{student_data['age']}")
print(f"Gender:\t\t{student_data['gender']}")
print("Courses:\t" + ", ".join(student_data["courses"]))
    

# Requirements:

#   Use `input()` to collect details.

#   Use dictionary operations `(dict[key] = value)` to store data.

#   Use `print()` formatting with `\n` and `\t` for better output.