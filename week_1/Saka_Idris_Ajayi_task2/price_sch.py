#=====Price display with type casting=====
#=========================================

# Ask the user for the price of garri per paint in naira(as a string) and convert it to float. 
# Display it with a message showing the amount in naira and kobo using print()



strPrice = input('Enter the price of Garri per paint in Naira: ')
floatPrice = float(strPrice)
print(f"The price of Garri per paint is N{floatPrice}")


# School registration form
stut_name = str(input("What is your fullname: "))
stut_class = str(input("What is your class: "))
stut_origin = str(input("What is your state of origin: "))

print("Student " + stut_name + " is in "  + stut_class + " is form " + stut_origin + ".")