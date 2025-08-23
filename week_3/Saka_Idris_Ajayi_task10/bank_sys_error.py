# TASK: Banking System – Runtime Errors

# g. FileNotFoundError: trying to load account file that doesn't exist
with open("accounts_data.txt", "r") as file:
    data = file.read()
