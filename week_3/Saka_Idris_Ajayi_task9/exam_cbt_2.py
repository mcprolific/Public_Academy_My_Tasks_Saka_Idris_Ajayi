# Subjects with Questions & Answers stored in Dictionary
questions = {
    "English": [
        {"question": "Choose the correct spelling:\n(a) Acommodate\n(b) Accommodate\n(c) Acomodate\n(d) Accomodate", "answer": "b"},
        {"question": "What is the synonym of 'benevolent'?\n(a) Kind\n(b) Angry\n(c) Cruel\n(d) Selfish", "answer": "a"},
        {"question": "Fill in the blank: She _____ to school every day.\n(a) go\n(b) goes\n(c) going\n(d) gone", "answer": "b"}
    ],
    "Maths": [
        {"question": "Solve: 12 + 8 * 2 = ?\n(a) 28\n(b) 32\n(c) 40\n(d) 44", "answer": "b"},
        {"question": "Simplify: 3x + 5x = ?\n(a) 15x\n(b) 8x\n(c) 2x\n(d) 5x", "answer": "b"},
        {"question": "Find the square root of 144:\n(a) 10\n(b) 11\n(c) 12\n(d) 14", "answer": "c"}
    ],
    "Physics": [
        {"question": "What is the SI unit of Force?\n(a) Watt\n(b) Pascal\n(c) Newton\n(d) Joule", "answer": "c"},
        {"question": "Light travels fastest in?\n(a) Water\n(b) Air\n(c) Vacuum\n(d) Glass", "answer": "c"},
        {"question": "What type of lens is used in a magnifying glass?\n(a) Concave\n(b) Convex\n(c) Plano\n(d) Diverging", "answer": "b"}
    ]
}

score = 0
total_questions = 0

print("\n*** WELCOME TO JAMB CBT EXAM 2025 ***")
print("Subjects: English, Maths and Physics")
print("Answer each question by typing a/b/c/d.\n")

# Go through each subject in order
for subject in ["English", "Maths", "Physics"]:
    print(f"\n--- {subject.upper()} SECTION ---")
    for i, q in enumerate(questions[subject], start=1):
        print(f"Q{i}: {q['question']}")
        ans = input("Your Answer (a/b/c/d): ").lower()
        total_questions += 1

        if ans == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct Answer: {q['answer']}\n")

# Show Final Results
print("\n*** EXAM COMPLETED ***")
print("Total Score:", score, "/", total_questions)
percentage = (score / total_questions) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage >= 70:
    print("Result: PASS")
else:
    print("Result: FAIL")
