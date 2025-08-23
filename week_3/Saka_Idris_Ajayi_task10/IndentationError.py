# TASK: Library Management – IndentationError
library = {
    "B001": {"title": "Python Basics", "author": "John"},
    "B002": {"title": "Data Science 101", "author": "Jane"}
}

for book_id in library:  # Missing proper indentation in loop body
print(library[book_id]["title"])  # This line should be indented
