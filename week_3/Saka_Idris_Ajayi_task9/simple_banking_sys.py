# TASK: Build a Simple Banking System (Dictionary-Based)

# Requirements:

# Use a dictionary to store customer accounts:
# accounts = {
#     "1001": {"name": "John Doe", "balance": 5000},
#     "1002": {"name": "Jane Smith", "balance": 10000}
# }

# Features to implement:
# Create New Account (auto-generate unique account numbers).
# Deposit Money (add to balance).
# Withdraw Money (ensure balance is sufficient).
# Check Balance.
# Transfer Money (between two accounts).
# View All Accounts.

# Input validations:
# Deposit/withdraw/transfer amounts must be positive.
# Cannot withdraw more than balance.

# Keep the menu running until the user exits.


accounts = {}
account_counter = 1000

while True:
    print("\n=== SIMPLE BANKING SYSTEM ===")
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. View All Accounts")
    print("7. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter account holder name: ").strip()
        balance = input("Enter initial deposit: ")
        if balance.isdigit() and int(balance) >= 0:
            account_counter += 1
            accounts[str(account_counter)] = {"name": name, "balance": int(balance)}
            print(f"Account created successfully! Account Number: {account_counter}")
        else:
            print("Invalid deposit amount.")

    elif choice == "2":
        acc = input("Enter account number: ")
        if acc in accounts:
            amt = input("Enter deposit amount: ")
            if amt.isdigit() and int(amt) > 0:
                accounts[acc]["balance"] += int(amt)
                print(f"Deposited {amt}. New Balance: {accounts[acc]['balance']}")
            else:
                print("Invalid amount.")
        else:
            print("Account not found.")

    elif choice == "3":
        acc = input("Enter account number: ")
        if acc in accounts:
            amt = input("Enter withdrawal amount: ")
            if amt.isdigit() and int(amt) > 0:
                amt = int(amt)
                if accounts[acc]["balance"] >= amt:
                    accounts[acc]["balance"] -= amt
                    print(f"Withdrawal successful. New Balance: {accounts[acc]['balance']}")
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid amount.")
        else:
            print("Account not found.")

    elif choice == "4":
        acc = input("Enter account number: ")
        if acc in accounts:
            print(f"Account Holder: {accounts[acc]['name']}, Balance: {accounts[acc]['balance']}")
        else:
            print("Account not found.")

    elif choice == "5":
        acc_from = input("Enter sender account number: ")
        acc_to = input("Enter receiver account number: ")
        amt = input("Enter amount to transfer: ")

        if acc_from in accounts and acc_to in accounts:
            if amt.isdigit() and int(amt) > 0:
                amt = int(amt)
                if accounts[acc_from]["balance"] >= amt:
                    accounts[acc_from]["balance"] -= amt
                    accounts[acc_to]["balance"] += amt
                    print(f"Transfer successful. New Balance of {acc_from}: {accounts[acc_from]['balance']}")
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid amount.")
        else:
            print("One or both accounts not found.")

    elif choice == "6":
        if accounts:
            print("\n--- All Accounts ---")
            for acc, data in accounts.items():
                print(f"Acc No: {acc}, Name: {data['name']}, Balance: {data['balance']}")
        else:
            print("No accounts available.")

    elif choice == "7":
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice. Try again.")
