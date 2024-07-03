import json
import os

FILE_PATH = "saving_user_data.json" # Define the file path for saving data


def load_data(): # Load data from file
    if os.path.exists(FILE_PATH): #load data from JSON file if it exists, otherwise return default data
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {"goals": [], "contributions": []} 


def save_data(data): # Save data to file
    with open(FILE_PATH, "w") as file:
        json.dump(data, file)