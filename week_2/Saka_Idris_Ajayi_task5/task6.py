print("Task6: Attendance Tracker \n")
print("A. Write a Python program that \n")
print("B. Stores the days of the week in a tuple. \n")

days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("This is days of week: " + ", ".join(days_of_week))

print("C. Stores the months of the year in another tuple. \n")

months_of_year = ("January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December")
print("This is months of year: " + ", ".join(months_of_year))

print("D. Asks the user to enter: \n")
#    Student’s name
student_name = input("Enter student's name: ")
#    Gender
gender = input("Enter gender: ")
#    Course Track
course_track = input("Enter course track: ")
#    Current month number (1-12)
month_num = int(input("Enter current month number (1-12): "))
#    Current day number (1-7)
day_num = int(input("Enter current day number (1-7): "))

# Print results
print("\nStudent's Name:", student_name)
print("Gender:", gender)
print("Course Track:", course_track)
print("Month Number:", month_num)
print("Day Number:", day_num)


