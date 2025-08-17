print("Compulsory Task: Student Profile Builder \n")

# Step 1
print("Collect personal details (name, age, gender). \n")
name = input("Enter student's full name: ")
age = int(input("Enter student's age: "))
gender = input("Enter student's gender: ")

# Step 2
print("Fixed subjects stored  \n") 
subjects = ("Math", "English", "Science")

# Step 3
print("Collect academic scores for a fixed set of subjects. \n")
scores = tuple(float(input(f"Enter score for {subj}: ")) for subj in subjects)

# Step 4
print("Store guardian information. \n")
guardian_name = input("Enter guardian's name: ")
guardian_phone = input("Enter guardian's phone number: ")

# Step 5
print("Store hobbies without duplicates. \n")
hobbies_input = input("Enter hobbies separated by commas: ")
# Expanded version of the set comprehension
hobbies_set = set()  # start with an empty set

for hob in hobbies_input.split(","):   # go through each entered hobby
    cleaned = hob.strip()       # remove extra spaces
    # list the ALL your hobbies one after the order
    # print("===============", cleaned)
    if cleaned:           # only keep non-empty values
        formatted = cleaned.title()  # format nicely in Title Case
        hobbies_set.add(formatted)   # add to the set (duplicates removed)

# convert the set into a list
hobbies_list = list(hobbies_set)


# Step 6
print("Automatically calculate average score and initials. \n")

# Dictionary comprehension pairing subjects ↔ scores
subject_scores = {}  # start with an empty dictionary

for subj, scindex in zip(subjects, scores):
    subject_scores[subj] = scindex   # assign each subject its score

# Step 7
# Get the first element (index 0) → Math score
math_score = scores[0]
# Get the second element (index 1) → English score
english_score = scores[1]
# Get the third element (index 2) → Science score
science_score = scores[2]

# Step 8
# Average score
# Step 8_1: Check if scores is not empty
if scores:
    # Step 8_2: Add up all the scores
    total = sum(scores)

    # Step 8_3: Count how many scores
    count = len(scores)

    # Step 8_4: Divide total by count to get the average
    average_score = total / count
else:
    # If there are no scores, set average to 0
    average_score = 0.0

# Step 9
# Initials from full name (first letter of each part)
# Split the name into parts (words)
parts = name.split()
# Create an empty string to store initials
initials = ""
# Go through each part of the name
for part in parts:
    if part:  # make sure it's not empty
        # Take the first letter, make it uppercase, and add it
        initials += part[0].upper()

# Step 10
# Hobbies count
hobby_count = len(hobbies_set)

# Step 11
print("--- Nested dictionaries for structure --- \n")
student_profile = {
    "personal": {
        "name": name,
        "age": age,
        "gender": gender,
        "initials": initials
    },
    "academics": {
        "subjects": subjects,                # tuple
        "scores": scores,                    # tuple
        "per_subject": subject_scores,       # dict via dict-comprehension + zip
        "average": round(average_score, 2)
    },
    "guardian": {
        "name": guardian_name,
        "phone": guardian_phone
    },
    "interests": {
        "hobbies": hobbies_list,             # list (deduped from set)
        "hobby_count": hobby_count
    }
}

# Step 12
print("--- Neat display using escape sequences --- \n")
print("\n===== STUDENT PROFILE =====")
print(f"Name:\t\t{name} ({initials})")
print(f"Age:\t\t{age}")
print(f"Gender:\t\t{gender}")

print("\n--- Academics ---")
for subj, acad in student_profile["academics"]["per_subject"].items():
    print(f"\t{subj}:\t{acad}")
print(f"\tAverage:\t{student_profile['academics']['average']}")

print("\n--- Guardian ---")
print(f"\tName:\t{student_profile['guardian']['name']}")
print(f"\tPhone:\t{student_profile['guardian']['phone']}")

print("\n--- Interests ---")
print(f"\tHobbies:\t{', '.join(student_profile['interests']['hobbies']) if hobbies_list else 'None'}")
print(f"\tTotal:\t\t{student_profile['interests']['hobby_count']}")

