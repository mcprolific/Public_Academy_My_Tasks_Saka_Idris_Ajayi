# Task4: Create a Unique Voters Registration System
voters = set()

# Ask for voter names and store in a set.
voter_name = int(input("Please specify how many voters will register: "))

# If a voter tries to register twice, display a warning.

for APC in range(voter_name):
    APC_name = input(f"Enter voter name {APC+1}: ")
    if APC_name in voters:
        print(f" {APC_name} is already registered!")
    else:
        voters.add(APC_name)
        print(f" {APC_name} registered successfully!")

# After registration, display the total number of unique voters.
print("\nTotal number of unique voters: ", len(voters))



