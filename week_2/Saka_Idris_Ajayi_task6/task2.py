# Task2: Unique Name Collector
#  - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.

# Create an empty set to store unique names
atted_seminar = set()

# Ask how many people to enter
num_by_person = int(input("How many names do you want to enter? "))

# Collect names
for McP in range(num_by_person):
    name = input(f"Enter name of attendee {McP+1}: ")
    atted_seminar.add(name.strip())  # .strip() removes extra spaces

# Display names in alphabetical order
print("\nAttendees in alphabetical order:")
for McP2 in sorted(atted_seminar):
    print(McP2)
