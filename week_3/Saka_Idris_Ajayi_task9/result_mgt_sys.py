# TASK: Build a Student Result Management System Using Dictionary

# Requirements:
# Create a program to store 10 students' names and their scores in 5 subjects (use dictionary).
# Compute and display for each student:

# Total Score
# Average Score
# Grade (A, B, C, D, F based on average)

# Display the best student (highest total) and the worst student (lowest total).
# Allow user to search for a student's result by name.
# Use loops to handle input and output neatly.



students = {}

print("=== STUDENT RESULT MANAGEMENT SYSTEM ===")

# INPUT 10 STUDENTS' DATA
for i in range(10):
    name = input(f"\nEnter name of student {i+1}: ").title()
    scores = []
    for j in range(5):
        score = int(input(f"Enter score for Subject {j+1} (0-100): "))
        while score < 0 or score > 100:
            score = int(input(f"Invalid! Enter score for Subject {j+1} (0-100): "))
        scores.append(score)
    students[name] = scores

# COMPUTE RESULTS
print("\n=== STUDENTS RESULTS ===")
best_student = ""
worst_student = ""
highest_total = -1
lowest_total = 500

for name, scores in students.items():
    total = sum(scores)
    average = total / 5
    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    print(f"\nName: {name}")
    print(f"Scores: {scores}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

    if total > highest_total:
        highest_total = total
        best_student = name

    if total < lowest_total:
        lowest_total = total
        worst_student = name

# DISPLAY BEST & WORST STUDENT
print(f"\nBest Student: {best_student} with Total Score: {highest_total}")
print(f"Worst Student: {worst_student} with Total Score: {lowest_total}")

# SEARCH FOR STUDENT'S RESULT
while True:
    search = input("\nEnter a student's name to view result (or type 'exit' to quit): ").title()
    if search.lower() == "exit":
        print("Exiting program. Goodbye!")
        break
    elif search in students:
        scores = students[search]
        total = sum(scores)
        average = total / 5
        if average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"
        print(f"\nName: {search}")
        print(f"Scores: {scores}")
        print(f"Total: {total}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
    else:
        print("Student not found!")

