# Task3: Simulate a football match ticket system

# Store all seat numbers (1 to 50) in a set.
empty_seats = set(range(1, 51))
print("Available seats number:", sorted(empty_seats))

# Ask users to "book" a seat by entering the number.
seat_book_per_person = int(input("Enter a seat number to book: "))

# Remove booked seats from the set.
empty_seats.remove(seat_book_per_person)


# Show remaining seats after each booking.
print("Remaining seats number:", sorted(empty_seats))

