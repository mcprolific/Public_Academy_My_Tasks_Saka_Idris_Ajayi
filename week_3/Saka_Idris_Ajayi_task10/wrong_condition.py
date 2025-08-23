# TASK: Student Result Management – Wrong pass/fail logic
students_scores = {"Saka": 99, "Janet": 75}

for name, score in students_scores.items():
    if score > 100:  # Wrong condition, nobody can score >100
        print(name, "Passed")
    else:
        print(name, "Failed")
