from colorama import init, Fore
from modules import data_manager
from modules import goal_manager
from modules import contribution_manager
from modules import report_manager

init(autoreset=True)

def main(): # Run main application loop, display the menu and handle user input
    data = data_manager.load_data()
    while True:
        print("\nMoney Saving Application")
        print(Fore.YELLOW + "1. Add new goal")
        print(Fore.MAGENTA + "2. Edit existing goal")
        print(Fore.YELLOW + "3. Delete a goal")
        print(Fore.MAGENTA + "4. List all your goals")
        print(Fore.YELLOW + "5. Contribute to your goal")
        print(Fore.MAGENTA + "6. View contribution history")
        print(Fore.YELLOW + "7. View your monthly saving report")
        print(Fore.RED + "\n8. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
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
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()