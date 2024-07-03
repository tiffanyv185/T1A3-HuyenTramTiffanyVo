import datetime # module to handle dates
from prettytable import PrettyTable # 3rd party library to display data in a table
from colorama import init, Fore, Style

init(autoreset=True)

def view_monthly_report(data): # allow users to view total contributions from a chosen month
    month = input("Enter the month for the report (YYYY-MM): ") # prompt user to enter the month for the report
    table = PrettyTable(["Goal", "Total Contributions"]) # initialise 'PrettyTable' with headers - Goal and Total Contributions
    report = {} # Initialise a dictionary to store the total contributions for each goal
    for contribution in data["contributions"]: # loop through all contributions
        if contribution["date"].startswith(month): # check if contribution date starts with user entered month
            if contribution["goal"] not in report: # initalise the total contributions for the goal if not already initialised
                report[contribution["goal"]] = 0
            report[contribution["goal"]] += contribution["amount"] # add contribution amount to the total for the goal
    for goal, total in report.items(): # add the total contribution for each goal to the table
        table.add_row([goal, total])
    print(table)



