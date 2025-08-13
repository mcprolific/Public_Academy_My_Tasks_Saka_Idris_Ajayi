#Transport fare calculator
#Ask for distance in kilometers
dist = float(input("Enter distance in km: "))

# Ask for fare per km
fare_per_km = float(input("Enter fare per km: "))

# Calculate total fare
total_fare = dist * fare_per_km

# Display total fare with two decimal places
print(f"Total fare is: ₦{total_fare:.2f}")
