from models import session, Task
from datetime import datetime, date
from tabulate import tabulate

PRIORITY_LEVELS = ["Low", "Medium", "High", "Critical"]

def list_tasks():
    tasks = session.query(Task).order_by(Task.due_date, Task.priority.desc()).all()
    if not tasks:
        print("📭 No tasks found.")
        return
    rows = [[
        t.id, t.title, t.due_date.strftime("%Y-%m-%d") if t.due_date else "N/A",
        t.priority, "✅" if t.completed else "❌",
        t.created_at.strftime("%Y-%m-%d %H:%M")
    ] for t in tasks]
    print(tabulate(rows, headers=["ID", "Title", "Due Date", "Priority", "Done", "Created At"], tablefmt="fancy_grid"))
