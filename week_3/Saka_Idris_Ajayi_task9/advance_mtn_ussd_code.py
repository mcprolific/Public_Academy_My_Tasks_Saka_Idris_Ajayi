print("\nWelcome to MTN USSD")
print("Enter one of these codes:")
print("*123# for Main Menu")
print("*131# for Data Menu")
print("*312# for Other Services")
print("0 to Exit\n")

# USSD Codes
ussd_codes = {
    "*123#": "Main Menu",
    "*131#": "Data Menu",
    "*312#": "Service Menu",
    "*321#": "Other Menu"
}
# 1. Account Info
# Account Info Submenu
account_info_menu = {
    1: "My Number",
    2: "My Tariff Plan",
    3: "My Account Balance",
    4: "My Data Balance",
    5: "End of Call Message",
    6: "Sim Registration Status",
    7: "Purchase History",
    0: "Back"
}

# Purchase History Submenu
purchase_history_menu = {
    1: "Store Locator",
    2: "SIM Swap",
    3: "Get your PUK number",
    4: "Block Stolen or Lost SIM",
    0: "Back"
}

# 2. Tariff Plans
# Purchase History Submenu
tariff_plans_menu = {
    1: "BetaGist",
    2: "Pulse",
    3: "Xtravalue",
    4: "XtraSpecial Postpaid",
    5: "MTN Broadband Tariff Plan",
    0: "Back",
    00: "Main Menu"
}
# BetaGist
beta_gist = {
    1: "Migrate to BetaGist",
    2: "BetaMix Bundle",
    3: "Use & Get Offer"
}
# a. Migrate to BetaGist
migrate_to_betaGist = {
    1: "Yes",
    0: "Back"
}

# b. BetaMix Bundle
betaMix_bundle = {
    1: "N50 Betamix Mini 40MB + 1min",
    2: "N100 Betamix Maxi 100MB + 2min",
    0: "Back"
}

# c. Use & Get Offer
use_get_offer = {
    1: "About Use & Get Offer",
    2: "Accumulated minutes & Get-back mins balance",
    0: "Back",
#     00: "MainMenu"
}

# Pulse


# Start Program Loop
while True:
    txtuscol = input("\nEnter your USSD Code: ")

    if txtuscol == "0":
        print("Exiting USSD Session...")
        break

    elif txtuscol == "*123#":  # Main Menu
        while True:
            print("\n--- MAIN MENU ---")
            print("1. Account Info")
            print("2. Tariff Plans")
            print("3. Data Services")
            print("4. Roaming/Int'l")
            print("5. My Services")
            print("6. Borrow Airtime/Data")
            print("7. Self Services")
            print("8. Chat Zigi")
            print("0. Back (End Session)")

            txtuscol_123 = int(input("Enter your number: "))
          # Starting code for Account Info
          # If the user press 1 then enter this
            if txtuscol_123 == 1:  # Account Info Menu
                while True:
                    print("\nMy Tools")
                    for key, value in account_info_menu.items():
                        print(f"{key}. {value}")

                    choice_info = int(input("Enter your number: "))

                    if choice_info == 1:
                        print("MTN - NG Message\nY'ello! Your mobile number is +234-813-3274-250")
                    elif choice_info == 2:
                        print("MTN - NG Message\nYou are currently on MTN Pulse Plan. Thank you!")
                    elif choice_info == 3:
                        print("MTN - NG Message\nYour main account balance: 10,000N")
                    elif choice_info == 4:
                        print("MTN - NG Message\nYour balances:\nData Bundle: 10.5GB\nMore details via SMS")
                    elif choice_info == 5:
                        print("1. Activate EOCN\n2. Deactivate EOCN")
                        exteocn = int(input("Enter your number: "))
                        if exteocn == 1:
                            print("You have activated EOCN")
                        elif exteocn == 2:
                            print("You have deactivated EOCN")
                        else:
                            print("Invalid input for EOCN")
                    elif choice_info == 6:
                        print("MTN - NG Message\nSystem Error")
                    elif choice_info == 7:  # Purchase History Menu
                        while True:
                            print("\n--- Purchase History ---")
                            for key, value in purchase_history_menu.items():
                                print(f"{key}. {value}")

                            pur_choice = int(input("Enter your number: "))

                            if pur_choice == 1:
                                print("This is your store locator for MTN")
                            elif pur_choice == 2:
                                print("This is your SIM Swap for MTN")
                            elif pur_choice == 3:
                                print("This is where you get your PUK number")
                            elif pur_choice == 4:
                                print("Your SIM has been blocked (stolen or lost)")
                            elif pur_choice == 0:
                                break  # Back to Account Info
                            else:
                                print("Invalid option for Purchase History")
                    elif choice_info == 0:
                        break  # Back to Main Menu
                    else:
                        print("Invalid option for Account Info")
          # Starting code for Tariff Plans
          # If the user press 2 then enter this
            elif txtuscol_123 == 2:  # Tariff Plans
                while True:
                    print("\nTariff Plans")
                    for key, value in tariff_plans_menu.items():
                        print(f"{key}. {value}")

                    choice_tariff = int(input("Enter your number: "))

                    if choice_tariff == 1:
                        while True:
                            print("n\BetaGist")
                            for key, value in beta_gist.items():
                                print(f"{key}. {value}")

                            choice_beta = int(input("Enter your number: "))

                            if choice_beta == 1:
                                while True:
                                    print("Enjoy a flat rate of 30k/sec to all networks in Nigeria. Also Get-back 3mins for every additional 6mins call from main account.\nProceed?")
                                    for key, value in migrate_to_betaGist.items():
                                        print(f"{key}. {value}")

                                    choice_beta_migrate = int(input("Enter your number: "))

                                    if choice_beta_migrate == 1:
                                        print("You are now migrated to Beta")
                                    elif choice_beta_migrate == 2:
                                        break  # Back to BetaGist
                                    else:
                                        print("Invalid option for Account Info")
                            elif choice_beta == 2:
                                while True:
                                    for key, value in betaMix_bundle.items():
                                        print(f"{key}. {value}")

                                    choice_betaMix_bundle = int(input("Enter your number: "))

                                    if choice_betaMix_bundle == 1:
                                        print("You will be migrated to BetaGist plan to purchase Betamix Bundle Mini. Do you wish to.\nProceed?")
                                        for key, value in migrate_to_betaGist.items():
                                             print(f"{key}. {value}")

                                        choice_beta_migrate = int(input("Enter your number: "))

                                        if choice_beta_migrate == 1:
                                             print("You are now migrated to Betamix Bundle Mini")
                                        elif choice_beta_migrate == 2:
                                             print("MTN - NG Message\nY'ellow! The migration request was cancelled successfully.\nThank you!")
                                        else:
                                             print("Invalid option for Account Info")
                                    elif choice_betaMix_bundle == 2:
                                        print("You will be migrated to BetaGist plan to purchase Betamix Bundle Max. Do you wish to.\nProceed?")
                                        for key, value in migrate_to_betaGist.items():
                                             print(f"{key}. {value}")

                                        choice_beta_migrate = int(input("Enter your number: "))

                                        if choice_beta_migrate == 1:
                                             print("You are now migrated to Betamix Bundle Max")
                                        elif choice_beta_migrate == 2:
                                             print("MTN - NG Message\nY'ellow! The migration request was cancelled successfully.\nThank you!")
                                        else:
                                             print("Invalid option for Account Info")

                                    elif choice_betaMix_bundle == 0:
                                        break  # Back to BetaGist
                                    else:
                                        print("Invalid option for Account Info")
                            elif choice_beta == 3:
                                while True:
                                    for key, value in use_get_offer.items():
                                        print(f"{key}. {value}")

                                    choice_use_get_offer = int(input("Enter your number: "))

                                    if choice_use_get_offer == 1:
                                        print("MTN - NG Message\nGet-back 3 mins for every 6 mins of calls made! You can accumulate up to 6000 minutes monthly. Your Get-back minutes are valid for 2 days")
                                    elif choice_use_get_offer == 2:
                                        print("MTN - NG Message\nDial *310*5# to check your accumulated and get-back minutes balance.")
                                    elif choice_use_get_offer == 0:
                                        break  # Back to BetaGist
                                   #  elif choice_use_get_offer == 00:
                                   #      break  # Back to BetaGist
                                   #      # break
                                    else:
                                        print("Invalid option for Account Info")                              
       
                    elif choice_tariff == 2:
                        print("MTN - NG Message\nYou are currently on MTN Pulse Plan. Thank you!")
                    elif choice_tariff == 3:
                        print("MTN - NG Message\nYour main account balance: 10,000N")
                    elif choice_tariff == 4:
                        print("MTN - NG Message\nYour balances:\nData Bundle: 10.5GB\nMore details via SMS")
                    elif choice_tariff == 5:
                        print("1. Activate EOCN\n2. Deactivate EOCN")
                        exteocn = int(input("Enter your number: "))
                        if exteocn == 1:
                            print("You have activated EOCN")
                        elif exteocn == 2:
                            print("You have deactivated EOCN")
                        else:
                            print("Invalid input for EOCN")
                    elif choice_tariff == 6:
                        print("MTN - NG Message\nSystem Error")
                    elif choice_tariff == 7:  # Purchase History Menu
                        while True:
                            print("\nPurchase History")
                            for key, value in purchase_history_menu.items():
                                print(f"{key}. {value}")

                            pur_choice = int(input("Enter your number: "))

                            if pur_choice == 1:
                                print("This is your store locator for MTN")
                            elif pur_choice == 2:
                                print("This is your SIM Swap for MTN")
                            elif pur_choice == 3:
                                print("This is where you get your PUK number")
                            elif pur_choice == 4:
                                print("Your SIM has been blocked (stolen or lost)")
                            elif pur_choice == 0:
                                break  # Back to Account Info
                            else:
                                print("Invalid option for Purchase History")
                    elif choice_tariff == 0:
                        break  # Back to Main Menu
                    else:
                        print("Invalid option for Account Info")

            elif txtuscol_123 == 0:
                break  # Exit Main Menu (Back to Enter USSD Code)
            else:
                print("Other main menu options are not implemented yet.")

    elif txtuscol in ussd_codes:
        print(f"You entered {txtuscol} ({ussd_codes[txtuscol]})")
    else:
        print("Invalid USSD Code.")
