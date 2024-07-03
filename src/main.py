from modules import data_manager
from modules import goal_manager
from modules import contribution_manager
from modules import report_manager

def main(): # Run main application loop, display the menu and handle user input
    data = data_manager.load_data()
    while True:
        print("\nMoney Saving Application")
        print("1. Add Goal")
        print("2. Edit Goal")
        print("3. Delete Goal")
        print("4. List Goals")
        print("5. Contribute to Goal")
        print("6. View Contribution History")
        print("7. View Monthly Report")
        print("8. Send Notifications")
        print("9. Exit")
        choice = input("Enter your choice: ")

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
            report_manager.send_notifications(data)
        elif choice == "9":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()