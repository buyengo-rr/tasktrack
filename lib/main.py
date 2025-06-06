from models import session, Task
from datetime import datetime, date
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

def list_tasks():
    tasks = session.query(Task).all()
    if not tasks:
        print("📭 No tasks found.")
        return
    rows = []
    for t in tasks:
        status = "✅" if t.completed else "❌"
        days_left = (t.due_date - date.today()).days
        if t.completed:
            color = Fore.GREEN
        elif t.due_date < date.today():
            color = Fore.RED
        else:
            color = Fore.YELLOW
        emoji = "🔴" if t.priority == "High" else "🟡" if t.priority == "Medium" else "🟢"
        rows.append([
            color + str(t.id) + Style.RESET_ALL,
            emoji + " " + t.title,
            t.due_date,
            status,
            t.priority,
            t.tags,
            f"{days_left} days" if days_left >= 0 else "Overdue"
        ])
    print(tabulate(rows, headers=["ID", "Title", "Due", "Done", "Priority", "Tags", "Time Left"], tablefmt="fancy_grid"))
