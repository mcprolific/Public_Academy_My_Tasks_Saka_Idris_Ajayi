while True:
    print("\n===== MULTIPLICATION TABLE GENERATOR =====")
    num = input("Enter a number to generate its multiplication table (or 'exit' to quit): ")

    if num.lower() == 'exit':
        print("Goodbye!")
        break

    if not num.isdigit():
        print("Invalid input! Please enter a valid number.")
        continue

    num = int(num)

    print(f"\nMultiplication Table for {num}")
    print("-" * 30)
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")
    print("-" * 30)
