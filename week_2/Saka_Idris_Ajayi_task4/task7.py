print("Task 7: List Manipulation \n")
print("A. Create a list of five cities. \n")
cities = ["Ogun", "Lagos", "Agbeloba", "Lantoro", "Ibadan"]
print(cities)

print("B. Replace the third city with a new one (entered by the user). \n")
newCity = input("Enter a new city to replace the third city: ")
cities[2] = newCity
print(cities)

print("C. Remove the last city. \n")
cities.pop()  # removes the last element
print(cities)

print("D. Add a new city to the beginning of the list. \n")
city_start = input("Enter a new city to add to the beginning of the list: ")
cities.insert(0, city_start)  # insert at index 0
print(cities)

print("E. Print the updated list. \n")
print("Updated list of cities:", cities)



