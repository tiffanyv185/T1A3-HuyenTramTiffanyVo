from prettytable import PrettyTable # 3rd party library to display information in table
from colorama import init, Fore, Style
from modules import data_manager # module to save goal data

init(autoreset=True)

def add_goal(data): # Prompt user to enter goal details and add the goal to the data
    name = input("What are you saving for? Enter your goal name: ") # ask user to enter goal name
    target = float(input("Enter the target amount: ")) # ask user to enter in target amount
    deadline = input("Enter the deadline (YYYY-MM-DD): ") # ask user to add a deadline
    goal = {"name": name, "target": target, "deadline": deadline, "saved": 0} # create goal dictionary with the initial saved amount of 0
    data["goals"].append(goal) # add the new goal to the list of goals in data
    data_manager.save_data(data) # save the updated data
    print(Fore.GREEN + Style.BRIGHT + "\nWoohoo! Goal added successfully. Good luck!")

def edit_goal(data): # List goals, prompt the user to select a goal and edit its details
    list_goals(data) # display the list of current goals
    goal_index = int(Fore.YELLOW + input("Enter the goal index to edit: ")) # prompt user to enter in index
    if 0 <= goal_index < len(data["goals"]): # ensure that entered index is valid
        goal = data["goals"][goal_index]
        goal["name"] = input(f"Enter the new name (current: {goal['name']}): ") or goal["name"] # prompt user to enter in new name or keep current name
        goal["target"] = float(input(f"Enter the new target (current: {goal['target']}): ") or goal["target"]) # prompt user to enter in new target or keep current target
        goal["deadline"] = input(f"Enter the new deadline (current: {goal['deadline']}): ") or goal["deadline"] # prompt user to enter in new deadline or keep current deadline
        data_manager.save_data(data) # save the updated data
        print(Fore.GREEN + Style.BRIGHT + "\nGoal edited successfully!")
    else:
        print(Fore.RED + "\nInvalid goal index!")

def delete_goal(data): # List goals, prompt user to select which goal to delete.
    list_goals(data) # list all current goals
    goal_index = int(input("Enter the goal index to delete: ")) # prompt user to enter in index that they want to delete
    if 0 <= goal_index < len(data["goals"]): # ensure that entered index is valid
        data["goals"].pop(goal_index) # remove the selected goal from list
        data_manager.save_data(data) # save the updated data
        print(Fore.GREEN + "\nGoal deleted successfully!")
    else:
        print(Fore.RED + "\nInvalid goal index!")

def list_goals(data): # display all goals in formatted table for user
    table = PrettyTable(["Index", "Name", "Target", "Deadline", "Saved", "Progress"]) # initialise 'PrettyTable' with the headers - Name, Target, Deadline, Saved, Progress
    for index, goal in enumerate(data["goals"]): # loop through each goal and add its details to the table
        progress = (goal["saved"] / goal["target"]) * 100
        table.add_row([index, goal["name"], goal["target"], goal["deadline"], goal["saved"], f"{progress:.2f}%"])
    print(table)