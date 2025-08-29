# TASK: Banking System – Wrong balance computation
accounts = {"1001": {"name": "Saka", "balance": 5,000,000}}

# Depositing 2000, but used subtraction instead of addition
accounts["1001"]["balance"] = accounts["1001"]["balance"] - 2000
print("Updated Balance:", accounts["1001"]["balance"])

