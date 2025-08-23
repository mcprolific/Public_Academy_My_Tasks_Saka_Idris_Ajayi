# TASK: Build a School Management System (Dictionary-Based)

# Requirements:

# Use a dictionary to store students' data:
# students = {
#     "101": {"name": "Saka", "age": 15, "class": "SS1", "scores": {"Math": 85, "English": 78}}
# }

# Features to implement:
# Add Student (auto-generate unique IDs).
# View All Students (display in a neat table format).
# Search Student by ID.
# Update Student Details (name, age, class, scores).
# Delete Student.
# Calculate Average Score for a specific student.

# Use a looped menu until the user exits.
# Validate inputs (age must be positive, scores between 0–100).


students = {}
next_id = 101

while True:
    print("\n=== SCHOOL MANAGEMENT SYSTEM ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Details")
    print("5. Delete Student")
    print("6. Calculate Average Score")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        while not age.isdigit() or int(age) <= 0:
            age = input("Invalid age! Enter a positive number: ")
        age = int(age)
        clas = input("Enter Class: ")
        scores = {}
        for subject in ["Math", "English", "Science", "Biology", "Chemistry"]:
            score = input(f"Enter score for {subject} (0-100): ")
            while not score.isdigit() or not (0 <= int(score) <= 100):
                score = input(f"Invalid! Enter score for {subject} (0-100): ")
            scores[subject] = int(score)
        students[str(next_id)] = {"name": name, "age": age, "class": clas, "scores": scores}
        print(f"Student Added Successfully! ID = {next_id}")
        next_id += 1

    elif choice == "2":
        if not students:
            print("No students found!")
        else:
            print("\nID\tName\tAge\tClass\tScores")
            for sid, details in students.items():
                print(f"{sid}\t{details['name']}\t{details['age']}\t{details['class']}\t{details['scores']}")

    elif choice == "3":
        sid = input("Enter Student ID to search: ")
        if sid in students:
            print(f"ID: {sid}, Name: {students[sid]['name']}, Age: {students[sid]['age']}, Class: {students[sid]['class']}, Scores: {students[sid]['scores']}")
        else:
            print("Student not found!")

    elif choice == "4":
        sid = input("Enter Student ID to update: ")
        if sid in students:
            print("Leave blank if no change.")
            name = input("Enter New Name: ")
            if name:
                students[sid]["name"] = name
            age = input("Enter New Age: ")
            if age.isdigit() and int(age) > 0:
                students[sid]["age"] = int(age)
            clas = input("Enter New Class: ")
            if clas:
                students[sid]["class"] = clas
            print("Do you want to update scores? (yes/no)")
            if input().lower() == "yes":
                for subject in students[sid]["scores"]:
                    score = input(f"Enter score for {subject} (0-100, leave blank to keep current): ")
                    if score.isdigit() and 0 <= int(score) <= 100:
                        students[sid]["scores"][subject] = int(score)
            print("Student Updated Successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        sid = input("Enter Student ID to delete: ")
        if sid in students:
            del students[sid]
            print("Student Deleted Successfully!")
        else:
            print("Student not found!")

    elif choice == "6":
        sid = input("Enter Student ID to calculate average score: ")
        if sid in students:
            scores = students[sid]["scores"]
            avg = sum(scores.values()) / len(scores)
            print(f"Average Score of {students[sid]['name']} is {avg:.2f}")
        else:
            print("Student not found!")

    elif choice == "7":
        print("Exiting Program. Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
