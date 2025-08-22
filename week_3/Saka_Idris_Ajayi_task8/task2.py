print("Task2")
# Comment the code below appropriately, and using doctring, explain what the code is doing.
# Adapt the code to the case below.

# Federal Government Scholarship Key Eligibility Requirements:
#   Citizenship:
#     Applicant must be a citizen of Nigeria. 
#   Enrollment:
#     Must be a registered, full-time undergraduate student in a recognized Nigerian university. 
#   Other Scholarships:
#     Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. 
#   Academic Qualification:
#     For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.

# Ask user to enter their names
name = input("Enter your name: ") 

# Ask user to enter their age
age = int(input("Enter your age: "))

# Ask user to enter their score from WAEC/WASSCE (May/June) exams
score = int(input("Enter your test score: "))

# Check if the user age and score are eligibility for Scholarship
eligibility = (age < 18) and (score > 70)

# Print out user information
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")