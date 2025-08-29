# USSD CODE
print("\n Welcome to MTN USSD")
print("Enter one of these codes:")
print("*123# for Main Menu")
print("*131# for Data Menu")
print("*312# for Other Services")
print("0 to Exit")

uscode_1 = "*123#"
uscode_2 = "*131#"
uscode_3 = "*312#"
uscode_4 = "*321#"




txtuscol = input("Enter your USSD Code: ")

if txtuscol == "*123#" :
    print("1. Account Info")
    print("2. Tariff Plans")
    print("3. Data Services")
    print("4. Roaming/Int'l")
    print("5. My Services")
    print("6. Borrow Airtime/Data")
    print("7. Self Services")
    print("8. Chat Zigi")

    txtuscol_123 = int(input("Enter your number: "))

    if txtuscol_123 == 1 :        # 1. Account Info
            print("My Tools \n")
            
            print("1. My Number")
            print("2. My Tariff Plan")
            print("3. My Account Balance")
            print("4. My Data Balance")
            print("5. End of Call Massage")
            print("6. Sim Registration Status")
            print("7. Purchase History")
            print("0. Back")

            txtuscol_123_mytools = int(input("Enter your number: "))

            if txtuscol_123_mytools == 1 :    # 1. My Number
                 print("MTN - NG Message  \nY'ello! Your mobile number is +234-813-3274-250")
            elif txtuscol_123_mytools == 2 :  # 2. Tariff Plans
                 print("MTN - NG Message  \nY'ello! You are currently on MTN Pulse Plan. \nThank you!")
            elif txtuscol_123_mytools == 3 :  # 3. My Account Balance
                 print("MTN - NG Message  \nYello! Your main account balance: 10,000N")
            elif txtuscol_123_mytools == 4 :  # 4. My Data Balance
                 print("MTN - NG Message  \nYour balances \nData Bundle: 10.5GB \n More details via SMS")
            elif txtuscol_123_mytools == 5 :  # 5. End of Call Massage
                 print("1. Activate EOCN \n2. Deactivate EOCN")

                 exteocn = int(input("Enter your number: "))

                 if exteocn == 1 : print("You are activate your EOCN")
                 elif exteocn == 2 : print("You are not activate your EOCN")
                 else : print("You are not follow our instruction for EOCN")
            elif txtuscol_123_mytools == 6 :  # 6. Sim Registration Status
                 print("MTN - NG Message  \nSystem Error")
            elif txtuscol_123_mytools == 7 :  # 7. Purchase History
                 print("1. Store Locator")
                 print("2. SIM Swap")
                 print("3. Get your PUK number")
                 print("4. Block Stolen or Lost SIM")
                 print("0. Black")

                 txtpurhis = int(input("Enter your number: "))

                 if txtpurhis == 1 : print("This is your store locator for MTN")
                 if txtpurhis == 2 : print("This is your SIM Swap for MTN")
                 if txtpurhis == 3 : print("This is the place to get your PUK number for MTN")
                 if txtpurhis == 4 : print("You SIM block stolen or lost for MTN")
                 else : print ("You are not follow our instruction for purchase history")
                 
                 
            elif txtuscol_123_mytools == 0 :  # 0. Back
               #   print()
                 exit()
            else :
                 print("You are not follow our instruction for My Tools")       # if users is not follow given instructions
                 
    elif txtuscol_123 == 2 :   # 2. Tariff Plans
         print("")
    elif txtuscol_123 == 3 :   # 3. My Account Balance
         print("")
    elif txtuscol_123 == 4 :   # 4. My Data Balance
         print("")
    elif txtuscol_123 == 5 :   # 5. My Services
         print("")
    elif txtuscol_123 == 6 :   # 6. Sim Registration Status
         print("")
    elif txtuscol_123 == 7 :   # 7. Self Services
         print("")
    elif txtuscol_123 == 8 :   # 8. Chat Zigi
         print("")
    else :
         print("You are not follow our instruction for USSD Code Number")       # if users is not follow given instructions

elif txtuscol == "*131#" :
    print("Your are type *131#....")
elif txtuscol == "*312#" :
    print("Your are type *321#....")
else : 
    print("Failure")
    exit()
    




