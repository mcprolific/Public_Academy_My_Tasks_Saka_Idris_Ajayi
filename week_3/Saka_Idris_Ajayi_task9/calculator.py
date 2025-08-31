import math

while True:
    print("\n===SIMPLE CALCULATOR===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root")
    print("6. Power/Exponent")
    print("7. Exit")


    choice = input("Choose an option (1-7): ")

    if choice == '7':
        print("Goodbye!")
        break

    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice! Please select a valid option.")
        continue

    try:
        if choice in ['1', '2', '3', '4', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        elif choice in ['5']:
            num1 = float(input("Enter square root number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
    elif choice == '5':
        print(f"Result: {num1} = {math.sqrt(num1)}")
    elif choice == '6':
        print(f"Result: {num1} ** {num2} = {num1 ** num2}")