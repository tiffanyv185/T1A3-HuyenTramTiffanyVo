import datetime
from prettytable import PrettyTable
import data_manager
import modules.goal_manager as goal_manager


def contribute(data): # List goals, prompt user to select a goal and contribute to it.
    goal_manager.list_goals(data)
    goal_index = int(input("Enter the goal index you want to contribute to: "))
    if 0 <= goal_index < len(data["goals"]):
        amount = float(input("Enter the amount you want to contribute: "))
        data["goals"][goal_index]["saved"] += amount
        contributtions = {"goal": data["goals"][goal_index]["name"], "amount": amount, "date": str(datetime.date.today())}
        data["contributions"].append(contribution)
        data_manager.save_data(data)
        print("Contribution added successfully!")
    else:
        print("Invalid goal index!")
    

    def view_history(data): # Display the history of all contributions in a table
        table = PrettyTable(["Goal", "Amount", "Date"])
        for contribution in data["contributions"]:
            table.add_row([contribution["goal"], contribution["amount"], contribution["date"]])
        print(table)