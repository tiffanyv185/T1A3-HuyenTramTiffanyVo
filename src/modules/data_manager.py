import json
import os


FILE_PATH = "saving_data.json"


def load_data():
    if os.path.exits(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return {"goals": [], "contributions": []}


def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file)