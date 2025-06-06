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
        days_left = (t.due_date - date.today()).days if t.due_date else None
        if t.completed:
            color = Fore.GREEN
        elif t.due_date and t.due_date < date.today():
            color = Fore.RED
        else:
            color = Fore.YELLOW
        emoji = "🔴" if t.priority == "High" else "🟡" if t.priority == "Medium" else "🟢"
        time_left = f"{days_left} days" if days_left is not None and days_left >= 0 else "Overdue" if days_left is not None else "No due date"
        created_str = t.created_at.strftime("%Y-%m-%d %H:%M")
        rows.append([
            color + str(t.id) + Style.RESET_ALL,
            emoji + " " + t.title,
            t.due_date or "N/A",
            created_str,
            status,
            t.priority,
            t.tags,
            time_left
        ])
    print(tabulate(rows, headers=["ID", "Title", "Due", "Created", "Done", "Priority", "Tags", "Time Left"], tablefmt="fancy_grid"))

def add_task():
    title = input("📝 Title: ")
    description = input("📄 Description: ")
    due_input = input("📆 Due Date (YYYY-MM-DD, optional): ")
    priority = input("⚡ Priority (Low/Medium/High): ")
    tags = input("🏷️ Tags (comma-separated): ")
    notes = input("🗒️ Notes (optional): ")
    due_date = None
    if due_input.strip():
        try:
            due_date = datetime.strptime(due_input, "%Y-%m-%d").date()
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.")
            return
    task = Task(
        title=title,
        description=description,
        due_date=due_date,
        priority=priority.capitalize() if priority else "Medium",
        tags=tags,
        notes=notes
    )
    session.add(task)
    session.commit()
    print("🎯 Task added!")

def view_task():
    task_id = input("🔍 Task ID: ")
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        created_str = task.created_at.strftime("%Y-%m-%d %H:%M")
        days_left = (task.due_date - date.today()).days if task.due_date else None
        time_left = f"{days_left} days" if days_left is not None and days_left >= 0 else "Overdue" if days_left is not None else "No due date"
        print(f"\n📌 {task.title}")
        print(f"🧾 {task.description}")
        print(f"📅 Due: {task.due_date or 'N/A'}")
        print(f"📅 Created: {created_str}")
        print(f"⚡ Priority: {task.priority}")
        print(f"🏷️ Tags: {task.tags}")
        print(f"🗒️ Notes: {task.notes}")
        print(f"⏳ Time Left: {time_left}")
        print(f"✅ Completed: {'Yes' if task.completed else 'No'}\n")
    else:
        print("❌ Task not found.")

def complete_task():
    task_id = input("✅ Mark complete - Task ID: ")
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        if task.completed:
            print("⚠️ Task already completed.")
        else:
            task.completed = True
            session.commit()
            print("🎉 Task completed!")
    else:
        print("❌ Task not found.")

def delete_task():
    task_id = input("🗑️ Delete - Task ID: ")
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        confirm = input(f"⚠️ Are you sure you want to delete task '{task.title}'? (y/n): ").lower()
        if confirm == 'y':
            session.delete(task)
            session.commit()
            print("🧹 Task deleted.")
        else:
            print("❌ Delete cancelled.")
    else:
        print("❌ Task not found.")

def upcoming_tasks():
    today = date.today()
    tasks = session.query(Task).filter(Task.due_date >= today, Task.completed == False).order_by(Task.due_date).all()
    if not tasks:
        print("🌞 No upcoming tasks.")
        return
    rows = []
    for t in tasks:
        days_left = (t.due_date - today).days if t.due_date else None
        emoji = "🔴" if t.priority == "High" else "🟡" if t.priority == "Medium" else "🟢"
        time_left = f"{days_left} days" if days_left is not None else "No due date"
        rows.append([
            t.id,
            emoji + " " + t.title,
            t.due_date or "N/A",
            t.priority,
            t.tags,
            time_left
        ])
    print(tabulate(rows, headers=["ID", "Title", "Due Date", "Priority", "Tags", "Time Left"], tablefmt="fancy_grid"))

def main():
    while True:
        print("\n⏳ TASKFLOW CLI")
        print("1. 📋 List Tasks")
        print("2. ➕ Add Task")
        print("3. 🔍 View Task")
        print("4. ✅ Mark as Complete")
        print("5. 🗑️ Delete Task")
        print("6. 📆 View Upcoming Tasks")
        print("0. 🚪 Exit")
        choice = input("Choose: ")
        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            view_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            upcoming_tasks()
        elif choice == "0":
            print("👋 Bye for now!")
            break
        else:
            print("❗ Invalid option.")

if __name__ == "__main__":
    main()
