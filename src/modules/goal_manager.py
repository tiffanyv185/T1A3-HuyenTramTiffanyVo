from prettytable import PrettyTable
from data_manager import save_data


def add_goal(date): # Prompt user to enter goal details and add the goal to the data
    name = input("What are you saving for? Enter your goal name: ")
    target = float(input("Enter the target amount: "))
    deadline = input("Enter the deadline (YYYY-MM-DD): ")
    goal = {"name": name, "target": target, "deadline": deadline, "saved": 0}
    data["goals"].append(goal)
    data_manager.save_data(data)
    print("Woohoo! Goal added successfully. Good luck!")
    

def edit_goal(data): # List goals, prompt the user to select a goal and edit its details
    list_goals(data)
    goal_index = int(input("Enter the goal index you wish to edit: "))
    if 0 <= goal_index < len(data["goals"]):
        goal = data_index["goals"][goal_index]
        goal["name"] = input(f"Enter a new name (current: {goal['name']}): ") or goal["name"]
        goal["target"] = float(input(f"Enter the new target (current: {goal['target']}): ") or goal["target"])
        goal["deadline"] = input(f"Enter the new deadline (current: {goal['deadline']}): ") or goal["deadline"]
        data_manager.save_data(data)
        print("Goal edited sucessfully!")
    else:
        print("Invalid goal index!")


def delete_goal(data): # List goals, prompt user to select which goal to delete.
    list_goals(data)
    goal_index = int(input("Enter the goal index you wish to delete: "))
    if 0 <= goal_index < len(data["goals"]):
        data["goals"].pop(goal_index)
        data_manager.save_data(data)
        print("Goal deleted successfully!")
    else:
        print("Invalid goal index!")


def list_goals(data): # display all goals in formatted table for user
    table = PrettyTable(["Index", "Name", "Target", "Deadline", "Saved", "Progress"])
    for index, goal in enumerate(data["goals"]):
        progress = (goal["saved"] / goal["target"]) * 100
        table.add_row([index, goal["name"], goal["deadline"], goal["saved"], f"{progress:.0f}%"])
    print(table)