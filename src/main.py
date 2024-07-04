# adds color to the terminal output; the menu
from colorama import init, Fore, Style
from modules import data_manager  # handles loading and saving data
from modules import goal_manager  # manages goals (add, edit, delete, list)
from modules import (
    contribution_manager,
)  # manages contributions and viewing of contribution history
from modules import report_manager  # generates monthly reports

init(autoreset=True)


def main():  # Run main application loop, display the menu and handle user input
    data = data_manager.load_data()
    while True:
        print(Style.BRIGHT + "\nMoney Saving Application")
        print(Fore.YELLOW + "\n1. Add new goal")
        print(Fore.MAGENTA + "2. Edit existing goal")
        print(Fore.YELLOW + "3. Delete a goal")
        print(Fore.MAGENTA + "4. List all your goals")
        print(Fore.YELLOW + "5. Contribute to your goal")
        print(Fore.MAGENTA + "6. View contribution history")
        print(Fore.YELLOW + "7. View your monthly saving report")
        print(Fore.RED + "\n8. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":  # handles user choices
            goal_manager.add_goal(data)
        elif choice == "2":
            goal_manager.edit_goal(data)
        elif choice == "3":
            goal_manager.delete_goal(data)
        elif choice == "4":
            goal_manager.list_goals(data)
        elif choice == "5":
            contribution_manager.contribute(data)
        elif choice == "6":
            contribution_manager.view_history(data)
        elif choice == "7":
            report_manager.view_monthly_report(data)
        elif choice == "8":
            print(Fore.RED + "\nExiting the application. Keep on saving!")
            break
        else:
            print("Invalid choice! Please try again.")


if (
    __name__ == "__main__"
):  # to ensure that the 'main()' function is only executed when the script is ran directly and not when it is imported as a module
    main()
