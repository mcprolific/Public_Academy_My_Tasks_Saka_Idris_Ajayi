from participant_pkg.file_ops import save_participant, load_participants


def get_participant_details():
    """Prompt user for participant details with validation."""
    print("\n=== Enter Participant Details ===")

    name = input("Enter Name: ").strip()

    # Validate age
    while True:
        try:
            age = int(input("Enter Age: ").strip())
            break
        except ValueError:
            print("Invalid age! Please enter a number.")

    phone = input("Enter Phone Number: ").strip()
    track = input("Enter Track (e.g., Python, AI Engineering): ").strip()

    return {"name": name, "age": age, "phone": phone, "track": track}


def main():
    """Main program loop."""
    file_path = "participants.csv"

    while True:
        print("\n=== Contact Saver Menu ===")
        print("1. Add Participant")
        print("2. View Participants")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            participant = get_participant_details()
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


if __name__ == "__main__":
    main()
