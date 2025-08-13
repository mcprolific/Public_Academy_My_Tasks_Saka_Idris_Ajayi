#=====Electricity bill formation=====
#====================================

# Ask for:
# customer's full name
# units consumed (kWh) - integer
# cost per unit - float


customer_name = input("Enter customer's full name: ")
units_consumed = int(input("Enter units consumed (kWh): "))
cost_per_unit = float(input("Enter cost per unit (₦): "))

# multiply here
total_bill = units_consumed * cost_per_unit

print("\n---== Publica Academy Electricity Bill ==---")
print(f"Customer Name: {customer_name}")
print(f"Units Consumed: {units_consumed}")
print(f"Cost per Unit: N{cost_per_unit:.2f}")
print(f"Total Amount Due: N{total_bill:.2f}")
