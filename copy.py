
def add_goal(data):  # Ask user to enter goal details
    name = input(
        "What are you saving for? Enter your goal name: "
    )  # ask user to enter goal name
    target = float(
        input("Enter the target amount: ")
    )  # ask user to enter in target amount
    # ask user to add a deadline
    deadline = input("Enter the deadline (YYYY-MM-DD): ")
    goal = {
        "name": name,
        "target": target,
        "deadline": deadline,
        "saved": 0,
    }  # create goal dictionary with the initial saved amount of 0
    data["goals"].append(goal)  # add the new goal to the list of goals in data
    data_manager.save_data(data)  # save the updated data
    print(
        Fore.GREEN +
        Style.BRIGHT +
        "\nWoohoo! Goal added successfully. Good luck!")