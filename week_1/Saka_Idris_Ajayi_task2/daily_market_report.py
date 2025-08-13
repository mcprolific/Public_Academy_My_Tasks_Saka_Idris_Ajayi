#=====Daily market report ask the user to input
#==============================================


mkt_name = input("Enter your market name: ")
num_trader = int(input("Enter your number traders: "))
daily_rev = int(input("Enter your daily revenue: "))

# Display the result using f-string formatting with commas for thousand separator
print(f"\nMarket Name: {mkt_name,}")
print(f"\nNumber of Traders: {num_trader,}")
print(f"\nDaily Revenue: {daily_rev,}")


