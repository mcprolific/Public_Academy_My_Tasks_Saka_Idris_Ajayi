# MTN USSD CODE
dial_1 = "*123#"
dial_2 = "*131#"

dial_choice = input("Enter your USSD Code for MTN: ")
if dial_choice == dial_1 :
    while True: 
        print("1. Account Info")
        print("2. Tariff Plans")
        print("3. Data Services")
        print("4. Roaming/Int'l")
        print("5. My Services")
        print("6. Borrow Airtime/Data")
        print("7. Self Services")
        print("8. Chat Zigi")

        choice_dial_1 = input("Enter choice: ")

        if choice_dial_1 == "1":
            print("My Tools: ")
            print("1. My Number")
            print("2. My Tariff Plain")
            print("3. My Account Balance")
            print("4. My Data Balance")
            print("5. End of call Message")
            print("6. Sim Registration Status")
            print("7. Purchase History")
            print("0. Back")

            choice_dial_1_MyTools = input("Enter choice: ")
            if choice_dial_1_MyTools == "1":
                print("MTN - NG Message")
                print("Y'ello Your mobile number is 2348133274250")
                # exit()
            elif choice_dial_1_MyTools == "2":
                print("MTN - NG Message")
                print("Y'ello You are currently on MTN Pulse plan")
                print("Thank you!")
            elif choice_dial_1_MyTools == "3":
                print("MTN - NG Message")
                print("Y'ello Your main account balance: 10,000N")
            elif choice_dial_1_MyTools == "4":
                print("MTN - NG Message")
                print("Your balances:")
                print("Data Bundle: 50GB")
                print("More details vis SMS.")
            elif choice_dial_1_MyTools == "5":
                print("End of call Message /n")
                print("1. Activate EOCN")
                print("2. Deactivate EOCN")
                
                choice_dial_1_MyToolsMe = input("Enter choice: ")
                if choice_dial_1_MyToolsMe == "1":
                    print("You are welcome to activate your EOCN")
                elif choice_dial_1_MyToolsMe == "2":
                    print("You are remove from EOCN")
                else:
                    print("Invalid option. Try again.")


            elif choice_dial_1_MyTools == "6":
                print("MTN - NG Message")
                print("system error")
            elif choice_dial_1_MyTools == "7":
                print("MTN - NG Message")
                print("system error")
            elif choice_dial_1_MyTools == "0":
                print("MTN - NG Message")
                print("system error")

                

            else:
              print("Invalid option. Try again.")






# # Do you remember this?

# balance = 1000  

# while True:
#     print("\nATM Menu:")
#     print("1. Check Balance")
#     print("2. Withdraw")
#     print("3. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         print(f"Your balance is: {balance}")
#     elif choice == "2":
#         amount = int(input("Enter withdrawal amount: "))
#         if amount <= balance:
#             balance -= amount
#             print(f"Withdrawal successful. New balance: {balance}")
#         else:
#             print("Insufficient funds.")
#     elif choice == "3":
#         print("Thank you for using our ATM. Goodbye!")
#         break
#     else:
#         print("Invalid option. Try again.")
