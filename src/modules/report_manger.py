import datetime
from prettytable import PrettyTable


def view_montly_report(data): # allow users to view total contributions from a chosen month
    month = input("Enter the month for the report (YYYY-MM): ")
    table = PrettyTable(["Goal", "Total Contributions"])
    report = {}
    for contributions in data["contributions"]:
        if contributions["date"].startswith(month):
            if contribution["goal"] not in report:
                report[contribution["goal"]] = 0
            report[contribution["goal"]] += contribution["amount"]
    for goal, total in report.items():
        table.add_row[(goal, total)]
    print(table)


def send_notifications(data): # Send user notifications for milestones achieved (if achieved) and upcoming deadlines
    today = datetime.date.today()
    for goal in data["goals"]:
        deadline = datetime.datetime.strptime(goal["deadline"], "%Y-%m-%d").date()
        if goal["saved"] >= goal["target"]:
            print(f"Congrats!! You've achieved your '{goal['name']} goal!")
        elif (deadline - today).days <= 7:
            print(f"The deadline for '{goal['name']}' goal is due on {goal['deadline']}!")

    