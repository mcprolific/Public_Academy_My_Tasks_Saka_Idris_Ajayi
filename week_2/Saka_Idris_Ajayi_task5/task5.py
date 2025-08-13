print("Task5: Modify Tuple Indirectly \n")
print("A. Ask a user to enter three items for their shopping list. \n")

shop_list1 = input(f"Enter the first shopping item: ")
shop_list2 = input(f"Enter the second shopping item: ")
shop_list3 = input(f"Enter the third shopping item: ")


print("B. Store in a tuple shopping_list. \n")
    # shop_lists.append(shop_list)
shop_All_list = [shop_list1, shop_list2, shop_list3]
print(shop_All_list)

print("C. Convert it to a list, then ask for two more items to add. \n")
shop_All_listMe = list(shop_All_list)
shop_list4 = input(f"Add another fourth shopping item: ")
shop_list5 = input(f"Add another fifth shopping item: ")
shop_All_listMe.append(shop_list4)
shop_All_listMe.append(shop_list5)



#   - Convert back to a tuple and print the updated list using join() to display items separated by " | ".

shop_All_tuple = tuple(shop_All_listMe)

print("Updated shopping list:", " | ".join(shop_All_tuple))

