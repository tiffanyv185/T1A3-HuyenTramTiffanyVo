import json  # module used for encoding and decoding JSON data
import os  # for interacting with the operating system, to check if file exists

FILE_PATH = "'user_data.json' "  # Define the file path for saving data


def load_data():  # Load data from file
    if os.path.exists(FILE_PATH):  # check if file JSON file exists
        with open(FILE_PATH, "r") as file:
            # if the file exists, it is opened in read mode and contents is
            # loaded using json.load(file)
            return json.load(file)
    # if JSON file does not exist, a default list structure with headings
    # "goals" and "contributions" is returned
    return {"goals": [], "contributions": [], }


def save_data(data):  # Save data to JSON file
    with open(FILE_PATH, "w") as file:  # the file is opened in write monde
        json.dump(data, file)  # the data os dumped into the file
