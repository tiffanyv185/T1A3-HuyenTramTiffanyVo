import json
import os

# Define the file path for saving data
FILE_PATH = "saving_data.json"

# Load data from file
def load_data():
    if os.path.exits(FILE_PATH): #if file already exists
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {"goals": [], "contributions": []} #create new file if one doesn't already exist

# Save data to file
def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file)