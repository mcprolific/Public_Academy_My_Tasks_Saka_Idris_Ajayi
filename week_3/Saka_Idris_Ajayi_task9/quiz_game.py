# TASK: Build a Quiz Game 

# Requirements:
# Store 20 multiple-choice questions (use a dictionary: {"question": "What is 2+2?", "options": ["A.2", "B.3", "C.4", "D.5"], "answer": "C"}).
# Randomly select 10 questions each time the game runs.
# Give the user 15 seconds per question to answer (if they don't answer in time, mark it wrong).
# Keep score and display result at the end (Correct answers, Wrong answers, Percentage).
# Allow user to retry the quiz without restarting the program.

questions = [
    {"question": "What is 2 + 2?", "options": ["A.2", "B.3", "C.4", "D.5"], "answer": "C"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A.Earth", "B.Mars", "C.Jupiter", "D.Saturn"], "answer": "B"},
    {"question": "What is the capital of France?", "options": ["A.London", "B.Rome", "C.Paris", "D.Madrid"], "answer": "C"},
    {"question": "Which is the largest ocean?", "options": ["A.Indian", "B.Pacific", "C.Atlantic", "D.Arctic"], "answer": "B"},
    {"question": "Which gas do plants absorb?", "options": ["A.Oxygen", "B.Nitrogen", "C.Carbon Dioxide", "D.Helium"], "answer": "C"},
    {"question": "What is H2O commonly known as?", "options": ["A.Hydrogen", "B.Oxygen", "C.Water", "D.Helium"], "answer": "C"},
    {"question": "Which country invented Pizza?", "options": ["A.France", "B.Italy", "C.USA", "D.Spain"], "answer": "B"},
    {"question": "What is the largest mammal?", "options": ["A.Elephant", "B.Blue Whale", "C.Giraffe", "D.Shark"], "answer": "B"},
    {"question": "How many continents are there?", "options": ["A.5", "B.6", "C.7", "D.8"], "answer": "C"},
    {"question": "Which instrument measures earthquakes?", "options": ["A.Barometer", "B.Seismograph", "C.Thermometer", "D.Hygrometer"], "answer": "B"},
    {"question": "Who painted Mona Lisa?", "options": ["A.Michelangelo", "B.Van Gogh", "C.Da Vinci", "D.Picasso"], "answer": "C"},
    {"question": "Which is the smallest prime number?", "options": ["A.0", "B.1", "C.2", "D.3"], "answer": "C"},
    {"question": "Which country is called the Land of the Rising Sun?", "options": ["A.China", "B.Japan", "C.Thailand", "D.Korea"], "answer": "B"},
    {"question": "How many sides does a hexagon have?", "options": ["A.5", "B.6", "C.7", "D.8"], "answer": "B"},
    {"question": "What is the boiling point of water?", "options": ["A.90°C", "B.95°C", "C.100°C", "D.110°C"], "answer": "C"},
    {"question": "Which planet has rings?", "options": ["A.Earth", "B.Mars", "C.Saturn", "D.Venus"], "answer": "C"},
    {"question": "Who discovered gravity?", "options": ["A.Newton", "B.Einstein", "C.Galileo", "D.Tesla"], "answer": "A"},
    {"question": "Which organ pumps blood?", "options": ["A.Brain", "B.Lungs", "C.Heart", "D.Kidney"], "answer": "C"},
    {"question": "Which element is needed for breathing?", "options": ["A.Helium", "B.Nitrogen", "C.Oxygen", "D.Carbon"], "answer": "C"},
    {"question": "What is the fastest land animal?", "options": ["A.Cheetah", "B.Lion", "C.Horse", "D.Tiger"], "answer": "A"}
]

retry = "yes"
while retry.lower() == "yes":
    correct = 0
    wrong = 0
    asked = []
    count = 0

    while count < 10:
        index = count  # sequential (no random)
        q = questions[index]
        print("\nQ", count + 1, ":", q["question"])
        for opt in q["options"]:
            print(opt)
        ans = input("Your answer (A/B/C/D): ").upper()

        if ans == q["answer"]:
            print("Correct!")
            correct += 1
        else:
            print("Wrong! Correct answer is", q["answer"])
            wrong += 1
        count += 1

    percentage = (correct / 10) * 100
    print("\nRESULT:")
    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Score:", percentage, "%")

    retry = input("\nDo you want to play again? (yes/no): ")
