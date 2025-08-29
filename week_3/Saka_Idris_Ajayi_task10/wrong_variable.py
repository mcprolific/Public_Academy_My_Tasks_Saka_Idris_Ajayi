# TASK: Library Management – Wrong book count
library = {"B001": {"title": "Python Basics", "copies": 3}}

borrowed_copies = 1
library["B001"]["copies"] = borrowed_copies  # Should subtract, not overwrite
print("Remaining copies:", library["B001"]["copies"])
