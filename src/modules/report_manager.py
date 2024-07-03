import datetime
from prettytable import PrettyTable


def view_monthly_report(data): # allow users to view total contributions from a chosen month
    month = input("Enter the month for the report (YYYY-MM): ")
    table = PrettyTable(["Goal", "Total Contributions"])
    report = {}
    for contribution in data["contributions"]:
        if contribution["date"].startswith(month):
            if contribution["goal"] not in report:
                report[contribution["goal"]] = 0
            report[contribution["goal"]] += contribution["amount"]
    for goal, total in report.items():
        table.add_row([goal, total])
    print(table)



    