# Syntax Errors

# a. IndentationError – Incorrect spacing
# b. Missing Colon/Parenthesis Error OR NameError
# c. Invalid Syntax – General grammar mistakes.


while True:

# a. IndentationError – Incorrect spacing
print("\n===== MULTIPLICATION TABLE GENERATOR =====")
    num = input("Enter a number to generate its multiplication table (or 'exit' to quit): ")

    if num.lower() == 'exit':
        print("Goodbye!")
        break

    if not num.isdigit():
        print("Invalid input! Please enter a valid number.")
        continue

    num = int(num)

    # b. Missing Colon/Parenthesis Error OR NameError
    print(f"\nMultiplication Table for {number}")

    # c. Invalid Syntax – General grammar mistakes.
    print "-" * 30
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")
    print("-" * 30)