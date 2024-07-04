import json # module used for encoding and decoding JSON data
import os # module used for interacting with the operating system, in this case, to check if the JSON file exists

FILE_PATH = "'user_data.json' " # Define the file path for saving data

def load_data(): # Load data from file
    if os.path.exists(FILE_PATH): # check if file JSON file exists
        with open(FILE_PATH, 'r') as file:
            return json.load(file) # if the file exists, it is opened in read mode and contents is loaded using json.load(file)
    return {"goals": [], "contributions": []} # if JSON file does not exist, a default list structure with headings "goals" and "contributions" is returned

def save_data(data): # Save data to JSON file
    with open(FILE_PATH, "w") as file: # the file is opened in write monde
        json.dump(data, file) #the data os dumped into the file