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
def add_task():
    title = input("📝 Title: ").strip()
    if not title:
        print("❌ Title cannot be empty.")
        return
    description = input("📄 Description: ").strip()
    due_input = input("📆 Due Date (YYYY-MM-DD) or leave empty: ").strip()
    due_date = None
    if due_input:
        try:
            due_date = datetime.strptime(due_input, "%Y-%m-%d").date()
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.")
            return
    print("Priority levels: Low, Medium, High, Critical")
    priority = input("⚡ Priority [Medium]: ").strip().capitalize()
    if priority not in PRIORITY_LEVELS:
        priority = "Medium"
    task = Task(title=title, description=description, due_date=due_date, priority=priority)
    session.add(task)
    session.commit()
    print("🎯 Task added!")


