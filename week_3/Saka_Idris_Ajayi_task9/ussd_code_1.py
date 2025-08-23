#===Simulated USSD Menu Interaction===
#=====================================

# step 1: Welcome screen
print("Welcome to Naija Mobile Service 🇳🇬")

# step 2: Ask customers to dial a USSD code
# This is for ZAIN
ussd_code = input("Please dial your USSD code (e.g., *123#): ")

# Step 3: Display menu options
print("Select an option:\n1. Check Balance\n2. Buy Airtime\n3. Buy Data")

# step 4: Ask user to choose an opti
choice = input("Enter option number (1, 2 or 3): ")

# step 5: Show confirmation message
print(f"You selected option {choice}")

# step 6: Ask for amount for options 2 or 3 (no checks)
amount = input("Enter amount (if applicable, else leave blank): ")

# step 7: Display final summary
print("Transaction Summary:")
print("USSD Code: " + ussd_code)
print("Selected Option: " + choice)
print("Amount: " + amount)
