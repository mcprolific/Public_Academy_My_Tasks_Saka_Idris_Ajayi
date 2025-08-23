# TASK: Library System – Runtime Errors

# e. IndexError: accessing a book list
books = ["Python Basics", "Data Science 101"]
print(books[5])  # index out of range

# f. KeyError: access missing key in dictionary
library = {"B001": {"title": "Python Basics", "author": "John"}}
print(library["B002"]["title"])  # KeyError
