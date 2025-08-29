from participant_pkg.file_ops import save_participant, load_participants

file_path = "participants.csv"

while True:
    print("\n=== Contact Saver Menu ===")
    print("1. Add Participant")
    print("2. View Participants")
    print("3. Exit")

    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        print("\n=== Enter Participant Details ===")
        # Check if the user type name or anything here, if not break the code means re asking the user
        while True:
            name = input("\tEnter Name: ").strip()
            if name:
                break
            print("\t[Error] Name cannot be empty. Please try again.")

        # Check if the user is write number or integer else re-asking the user again 
        while True:
            try:
                age = int(input("Enter Age: ").strip())
                break
            except ValueError:
                print("Invalid age! Please enter a number.")

        # Is the same to the this phone number
        while True:
            phone = input("\tEnter Phone Number: ").strip()
            if len(phone) == 11 and phone.isdigit():
                break
            print("\t[Error] Phone number must be 11 digits.")

        while True:
            track = input("\tEnter Track (e.g., AI Developer, AI Engineering): ").strip()
            if track:
                break
            print("\t[Error] Track cannot be empty.")
        # This is the dictionary code, you can still say object array
        participant = {"name": name, "age": age, "phone": phone, "track": track}

        save_participant(file_path, participant)
        print("\nParticipant saved successfully!")

    elif choice == "2":
        participants = load_participants(file_path)
        if participants:
            print("\n=== Participants List ===")
            for idx, p in enumerate(participants, start=1):
                print(f"{idx}. {p['name']} (Age: {p['age']}, Phone: {p['phone']}, Track: {p['track']})")
        else:
            print("\nNo participants found.")

    elif choice == "3":
        print("\nExiting... Goodbye!")
        break
    else:
        print("\nInvalid choice, please select 1–3.")

# ======Good Luck! to my group member ========
