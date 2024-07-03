import datetime # module for handling dates
from prettytable import PrettyTable # 3rd party library for displaying data in a table
from modules import data_manager # module to save data after making a contribution
from modules import goal_manager # module to list goals when making a contribution

def contribute(data): # List goals, prompt user to select a goal and contribute to it.
    goal_manager.list_goals(data) # list the existing goals
    goal_index = int(input("Enter the goal index you want to contribute to: ")) # prompt user to enter in index
    if 0 <= goal_index < len(data["goals"]): # check if the user entered index is valid
        amount = float(input("Enter the amount you want to contribute: "))
        data["goals"][goal_index]["saved"] += amount # update the saved amount for the goal
        contribution = {"goal": data["goals"][goal_index]["name"], "amount": amount, "date": str(datetime.date.today())} # create a contribution record
        data["contributions"].append(contribution) # add the contribution record to the contributions list
        data_manager.save_data(data) # save the contribution data
        print("Contribution added successfully!")
    else:
        print("Invalid goal index!")
    
def view_history(data): # Display the history of all contributions in a table#
    table = PrettyTable(["Goal", "Amount", "Date"]) # create a table with the headers (goal, amount and date)
    for contribution in data["contributions"]:
        table.add_row([contribution["goal"], contribution["amount"], contribution["date"]])
    print(table) # print table for users to view