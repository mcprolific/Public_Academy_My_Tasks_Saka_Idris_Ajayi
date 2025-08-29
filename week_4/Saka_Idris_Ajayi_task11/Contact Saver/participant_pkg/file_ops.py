# ======= GENERAL NOTICES==============
# IF YOU WANT TO DO THIS WORK 
# GOTO Working_wih_files2, then check this
# Working with CSV Files -Spreadsheet like Data
# ===============================================


# CSV files are like simple spreadsheets. They are perfect for storing data in rows and columns.
import csv

# Python has a modern library called `pathlib`, which is easier to use than `os`.
from pathlib import Path



#  This appends participant details to a CSV file (creates the file and writes
def save_participant(path, participant_dict):
# Create an input file with some text
# I use this example from "Working with Multiple Files at Once"
# A docstring is a special string (inside triple quotes) placed just below a function, class, or module definition.
# It is not executed as code — it is just documentation that lives inside the function.
    """
    Save a participant's details into a CSV file.
    If the file doesn't exist, create it and add a header row.
    """

# Converts the string path into a Path object.
    file_jenat = Path(path)

# A header if it doesn’t exist)
    try:
        # Check if file exists
        file_jenat_exists = file_jenat.exists()

        # Open in append mode
        # Write data to CSV file
        with open(file_jenat, "a", newline="", encoding="utf-8") as jenat_csv:
            writer = csv.writer(jenat_csv)

            # Write header if file is new
            if not file_jenat_exists:
                # Write all rows at once
                writer.writerow(["name", "age", "phone", "track"])   

            # Write participant details (ensure correct order)
            # This is calling the writerow method from Python’s csv.writer.
            # participant_dict is a dictionary holding participant details, e.g.: {"name": "Jenat", "age": 99, "phone": "08133274250", "track": "AI Developer"}
            writer.writerow([
                participant_dict.get("name", ""),
                participant_dict.get("age", ""),
                participant_dict.get("phone", ""),
                participant_dict.get("track", "")
            ])

    except Exception as e:
        print(f"Participant record could not be saved: {e}")

#  ///////////////// STEP TWO ///////////////
def load_participants(file_path):
    """
    Load all participants' details from a CSV file.
    Returns a list of dictionaries.
    """

    # Create empty data
    participants = []
    try:
        idris_file = Path(file_path)

        if not idris_file.exists():
            return participants  # return empty list if file not found

        # Read the CSV file back
        with open(idris_file, "r", encoding="utf-8") as idris_csv:
            reader = csv.reader(idris_csv)
            headers = next(reader, None)  # first row = header

            if headers:
                for row in reader:
                    participants.append(dict(zip(headers, row)))

    except Exception as e:
        print(f"Error loading participants: {e}")

    return participants
