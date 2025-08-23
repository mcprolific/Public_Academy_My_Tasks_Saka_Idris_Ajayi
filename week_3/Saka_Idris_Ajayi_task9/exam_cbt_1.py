print("=== WELCOME TO JAMB 2025 CBT EXAM ===\n")
print("INSTRUCTIONS:")
print("1. There are 5 questions.")
print("2. Each question carries 1 mark.")
print("3. Select the correct option (A, B, C, or D).\n")

score = 0

# Question 1
print("1. What is the capital of Nigeria?")
print("A. Lagos")
print("B. Abuja")
print("C. Port Harcourt")
print("D. Ibadan")
answer = input("Your Answer: ").upper()
if answer == "B":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is B. Abuja\n")

# Question 2
print("2. Which of the following is NOT a programming language?")
print("A. Python")
print("B. Java")
print("C. HTML")
print("D. C++")
answer = input("Your Answer: ").upper()
if answer == "C":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is C. HTML\n")

# Question 3
print("3. Who is the current Secretary-General of the United Nations (2025)?")
print("A. Ban Ki-moon")
print("B. António Guterres")
print("C. Kofi Annan")
print("D. Boutros Boutros-Ghali")
answer = input("Your Answer: ").upper()
if answer == "B":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is B. António Guterres\n")

# Question 4
print("4. What is the chemical symbol of Gold?")
print("A. Ag")
print("B. Au")
print("C. Pb")
print("D. Go")
answer = input("Your Answer: ").upper()
if answer == "B":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is B. Au\n")

# Question 5
print("5. Solve: 12 * 5 - 10 = ?")
print("A. 50")
print("B. 55")
print("C. 60")
print("D. 40")
answer = input("Your Answer: ").upper()
if answer == "A":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is A. 50\n")

# Final Score
print(f"EXAM COMPLETED! \nYour Total Score: {score}/5")
if score == 5:
    print("Excellent! You got all answers correct!")
elif score >= 3:
    print("Good job! You passed.")
else:
    print("You need to improve. Try again!")
