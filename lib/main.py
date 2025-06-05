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
def view_task():
    try:
        task_id = int(input("🔍 Task ID: ").strip())
    except ValueError:
        print("❌ Invalid ID format.")
        return
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        print(f"\n📌 {task.title}")
        print(f"🧾 Description: {task.description or 'N/A'}")
        print(f"📅 Due Date: {task.due_date.strftime('%Y-%m-%d') if task.due_date else 'N/A'}")
        print(f"⚡ Priority: {task.priority}")
        print(f"✅ Completed: {'Yes' if task.completed else 'No'}")
        print(f"🕒 Created At: {task.created_at.strftime('%Y-%m-%d %H:%M')}")
        print(f"🕒 Last Updated: {task.updated_at.strftime('%Y-%m-%d %H:%M')}\n")
    else:
        print("❌ Task not found.")
def complete_task():
    try:
        task_id = int(input("✅ Mark complete - Task ID: ").strip())
    except ValueError:
        print("❌ Invalid ID format.")
        return
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        if task.completed:
            print("✅ Task is already marked complete.")
        else:
            task.completed = True
            session.commit()
            print("🎉 Task completed!")
    else:
        print("❌ Task not found.")
def delete_task():
    try:
        task_id = int(input("🗑️ Delete - Task ID: ").strip())
    except ValueError:
        print("❌ Invalid ID format.")
        return
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        confirm = input(f"Are you sure you want to delete task '{task.title}'? (y/N): ").strip().lower()
        if confirm == 'y':
            session.delete(task)
            session.commit()
            print("🧹 Task deleted.")
        else:
            print("🛑 Deletion cancelled.")
    else:
        print("❌ Task not found.")
def upcoming_tasks():
    today = date.today()
    tasks = session.query(Task).filter(Task.due_date >= today, Task.completed == False).order_by(Task.due_date, Task.priority.desc()).all()
    if not tasks:
        print("🌞 No upcoming tasks.")
        return
    rows = [[
        t.id, t.title,
        t.due_date.strftime("%Y-%m-%d"),
        t.priority
    ] for t in tasks]
    print(tabulate(rows, headers=["ID", "Title", "Due Date", "Priority"], tablefmt="fancy_grid"))
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
        
        choice = input("Choose: ").strip()

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


