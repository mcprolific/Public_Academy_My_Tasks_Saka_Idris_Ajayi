#====School Fees Breakdown====
#=============================

# Inputs
school_name = input("Enter school name: ")
tuition_fee = float(input("Enter tuition fee: "))
hostel_fee = float(input("Enter hostel fee: "))
feeding_fee = float(input("Enter feeding fee: "))

# Calculate total fee
total_fee = tuition_fee + hostel_fee + feeding_fee

# Print receipt with each fee on a new line
print(f"\n--- {school_name} Fees Receipt ---")
print(f"Tuition Fee: N{tuition_fee:.2f}")
print(f"Hostel Fee: N{hostel_fee:.2f}")
print(f"Feeding Fee: N{feeding_fee:.2f}")
print(f"Total Fee: N{total_fee:.2f}")
