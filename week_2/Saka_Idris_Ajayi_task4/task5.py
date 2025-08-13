# METHOD 1

print("Task 5: Student Score Tracker \n")

print("A: Ask the user for 3 student names. \n")

stutName_1 = str(input("Enter first student name: "))
stutName_2 = str(input("Enter second student name: "))
stutName_3 = str(input("Enter third student name: "))

print("====List of Students====")
print("1. " + stutName_1 + "\n" + "2. " + stutName_2 + "\n" + "3. " + stutName_3 )

print("B: For each student, ask for their score. \n")
stutScore_1 = input("Enter the score for " + stutName_1 + ": " )
stutScore_2 = input("Enter the score for " + stutName_2 + ": " )
stutScore_3 = input("Enter the score for " + stutName_3 + ": " )

print("C: Store the results in two lists (one for names, one for scores). \n")

storeRes_1 = ('1.' + stutName_1 +'           ' + stutScore_1)
storeRes_2 = ('2.' + stutName_2 +'           ' + stutScore_2)
storeRes_3 = ('3.'+ stutName_3 +'           '  + stutScore_3)


print("D: Print a formatted output showing Name — Score, aligned neatly. \n")
print("\nStudent Score Tracker")
print("-" * 30)
print("S/N" + "Student Name" + "      " + "Student Scores")
print(storeRes_1)
print(storeRes_2)
print(storeRes_3)



print("E: Tips: You are to start by creating two empty lists. \n")

# METHOD 2

# Create empty lists
names = []
scores = []

# Ask for 3 student names and scores
for i in range(3):
    name = input(f"Enter the name of student {i+1}: ")
    score = float(input(f"Enter the score for {name}: "))

    names.append(name)
    scores.append(score)

# Print formatted output
print("\nStudent Score Tracker")
print("-" * 30)
print(f"{'Name':<15} {'Score':>10}")
print("-" * 30)

for i in range(3):
    print(f"{names[i]:<15} {scores[i]:>10}")
