print("Task 4: Name Organizer \n")

print("A: Ask the user to enter 5 names (separated by spaces). \n")
valname1 = input("Enter five names separated by spaces: ")
print(valname1)

print("B: Convert all names to lowercase. \n")
print(valname1.lower())


print("C: Sort the list alphabetically. \n")
listAlp = valname1.split()
listAlp.sort()


print("D: Display them one name per line.  Tips: use `range()`,`sort()`, `for`, `in`, `split()`, `len()`,`lower()` \n")

print("\nSorted names:")
for valname1 in listAlp:
    print(valname1)
