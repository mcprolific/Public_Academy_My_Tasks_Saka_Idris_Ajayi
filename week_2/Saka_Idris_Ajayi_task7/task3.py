print("Task3: Days and Activities Pairing \n")
print("A. Store days of the week in a tuple \n")

days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


print("This is days of week: " + ", ".join(days_of_week))

print("Ask the user to input an activity for three specific days.  \n")
day1 = input("Choose a day (e.g., Monday): ")
activity1 = input(f"What activity will you do on {day1}? ")

day2 = input("Choose another day: ")
activity2 = input(f"What activity will you do on {day2}? ")

day3 = input("Choose another day: ")
activity3 = input(f"What activity will you do on {day3}? ")

print("B. Use dictionary comprehension to pair days and activities. \n")  
selected_days = (day1, day2, day3)
activities = (activity1, activity2, activity3)

schedule = {day: activity for day, activity in zip(selected_days, activities)}


#   Print the dictionary.

print("\n===== Your Weekly Activity Schedule =====")
print(schedule)

# Requirements:

#   Use a tuple for days.

#   Use {day: activity for day, activity in `zip(..., ...)`}.
#   Tip: Research on how to use `zip()`
