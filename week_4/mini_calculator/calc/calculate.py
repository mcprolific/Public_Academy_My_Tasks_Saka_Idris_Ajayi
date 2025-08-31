from calc import calc_operations
def calculator():        
    # Display available operations to the user

    print("Select operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exponent/Power")
    print("0. Exit")

    # Now we let the user choose which operation they want to perform by using an input statement
    while True:
        try:
            choice = int(input("Enter choice(1, 2, 3, 4, 5, 6 or 0 to exit): "))
            # In the next two lines, we receive values for the two numbers from the user
            if choice == 0:
                break
            elif choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 6:
                num1 = float(input("Enter a first number: "))
                num2 = float(input("Enter a second number: "))
            elif choice == 5:
                num = float(input("Enter the number: "))
            else:
                pass
            
        except Exception as e:
            print(e)
            print("Please input a psotive number in the range of 1 - 4")
            continue
        
        if choice == 1:
            print(f"The result of {num1} + {num2} is {calc_operations.add(num1, num2)}")
        elif choice == 2:
            print(f"The result of {num1} - {num2} is {calc_operations.subtract(num1, num2)}")
        elif choice == 3:
            print(f"The result of {num1} * {num2} is {calc_operations.multiply(num1, num2)}")
        elif choice == 4:
            print(f"The result of {num1} / {num2} is {calc_operations.divide(num1, num2)}")
        elif choice == 5:
            print(f"The square root of {num} is {calc_operations.sqrt(num)}")
        elif choice == 6:
            print(f"{num1} ** {num2} = {calc_operations.exp(num1, num2)}")
        
        else:
            print("Invalid input. Please choose a number from 1 - 4")
        
        
