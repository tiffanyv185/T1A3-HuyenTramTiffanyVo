import datetime  # module for handling dates
# 3rd party library for displaying data in a table
from prettytable import PrettyTable
from colorama import init, Fore, Style
from modules import data_manager  # save data after making a contribution
from modules import goal_manager  # list goals when making a contribution

init(autoreset=True)


# List goals, prompt user to select a goal and contribute to it.
def contribute(data):
    goal_manager.list_goals(data)  # list the existing goals
    goal_index = int(
        input("Enter the goal index you want to contribute to: ")
    )  # prompt user to enter in index
    if 0 <= goal_index < len(
            data["goals"]):  # check if the user entered index is valid
        amount = float(input("Enter the amount you want to contribute: "))
        data["goals"][goal_index][
            "saved"
        ] += amount  # update the saved amount for the goal
        contribution = {
            "goal": data["goals"][goal_index]["name"],
            "amount": amount,
            "date": str(datetime.date.today()),
        }  # create a contribution record
        data["contributions"].append(
            contribution
        )  # add the contribution record to the contributions list
        data_manager.save_data(data)  # save the contribution data
        print(Fore.GREEN + Style.BRIGHT + "Contribution added successfully!")
    else:
        print(Fore.RED + "Invalid goal index!")


def view_history(data):  # Display the history of all contributions in a table#
    table = PrettyTable(
        ["Goal", "Amount", "Date"]
    )  # create a table with the headers (goal, amount and date)
    for contribution in data["contributions"]:
        table.add_row([contribution["goal"],
                       contribution["amount"],
                       contribution["date"]])
    print(table)  # print table for users to view
