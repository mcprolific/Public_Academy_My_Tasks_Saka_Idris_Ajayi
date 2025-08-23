# TASK: Build a Library Management System (Dictionary-Based)

# Requirements:

# Use a dictionary to store books in the library:

# library = {
#     "B001": {"title": "Python Basics", "author": "John Doe", "copies": 3},
#     "B002": {"title": "Data Science 101", "author": "Jane Smith", "copies": 5}
# }


# Features to implement:
# Add a New Book (auto-generate book IDs).
# Borrow a Book (reduce available copies, ensure copies > 0).
# Return a Book (increase available copies).
# Search for a Book by Title or Author.
# View All Books (show ID, title, author, and available copies).

# Input validations:
# Cannot borrow a book with 0 available copies.
# Cannot add a book with negative copies.

# Program should keep running until the user exits.


import random

# Initial library data
library = {
    "B001": {"title": "Python Basics", "author": "John Doe", "copies": 3},
    "B002": {"title": "Data Science 101", "author": "Jane Smith", "copies": 5}
}

def generate_book_id():
    return "B" + str(random.randint(100, 999))

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    try:
        copies = int(input("Enter number of copies: "))
        if copies < 0:
            print("Copies cannot be negative!")
            return
    except ValueError:
        print("Invalid input! Copies must be a number.")
        return

    book_id = generate_book_id()
    library[book_id] = {"title": title, "author": author, "copies": copies}
    print(f"Book added successfully with ID {book_id}")

def borrow_book():
    book_id = input("Enter book ID to borrow: ").upper()
    if book_id in library:
        if library[book_id]["copies"] > 0:
            library[book_id]["copies"] -= 1
            print(f"You borrowed '{library[book_id]['title']}'. Copies left: {library[book_id]['copies']}")
        else:
            print("Sorry, no copies available!")
    else:
        print("Book not found!")

def return_book():
    book_id = input("Enter book ID to return: ").upper()
    if book_id in library:
        library[book_id]["copies"] += 1
        print(f"Book '{library[book_id]['title']}' returned successfully.")
    else:
        print("Book not found!")

def search_book():
    keyword = input("Enter title or author to search: ").lower()
    found = False
    for book_id, details in library.items():
        if keyword in details["title"].lower() or keyword in details["author"].lower():
            print(f"{book_id} - {details['title']} by {details['author']} (Copies: {details['copies']})")
            found = True
    if not found:
        print("No matching books found.")

def view_books():
    print("\n--- Library Books ---")
    if not library:
        print("No books in the library.")
    else:
        for book_id, details in library.items():
            print(f"{book_id}: {details['title']} by {details['author']} (Copies: {details['copies']})")
    print("---------------------\n")

# Main Menu
while True:
    print("\nLibrary Management System")
    print("1. Add New Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View All Books")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        borrow_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        view_books()
    elif choice == "6":
        print("Exiting Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
