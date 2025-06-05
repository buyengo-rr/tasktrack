from models import session, Task
from datetime import datetime, date
from tabulate import tabulate

def list_tasks():
    tasks = session.query(Task).all()
    if not tasks:
        print("📭 No tasks found.")
        return
    rows = [[t.id, t.title, t.due_date, "✅" if t.completed else "❌"] for t in tasks]
    print(tabulate(rows, headers=["ID", "Title", "Due Date", "Done"], tablefmt="fancy_grid"))

def add_task():
    title = input("📝 Title: ")
    description = input("📄 Description: ")
    due_input = input("📆 Due Date (YYYY-MM-DD): ")
    try:
        due_date = datetime.strptime(due_input, "%Y-%m-%d").date()
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")
        return
    task = Task(title=title, description=description, due_date=due_date)
    session.add(task)
    session.commit()
    print("🎯 Task added!")

def view_task():
    task_id = input("🔍 Task ID: ")
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        print(f"\n📌 {task.title}")
        print(f"🧾 {task.description}")
        print(f"📅 Due: {task.due_date}")
        print(f"✅ Completed: {'Yes' if task.completed else 'No'}\n")
    else:
        print("❌ Task not found.")

def complete_task():
    task_id = input("✅ Mark complete - Task ID: ")
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        task.completed = True
        session.commit()
        print("🎉 Task completed!")
    else:
        print("❌ Task not found.")

def delete_task():
    task_id = input("🗑️ Delete - Task ID: ")
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print("🧹 Task deleted.")
    else:
        print("❌ Task not found.")

def upcoming_tasks():
    today = date.today()
    tasks = session.query(Task).filter(Task.due_date >= today, Task.completed == False).order_by(Task.due_date).all()
    if not tasks:
        print("🌞 No upcoming tasks.")
        return
    rows = [[t.id, t.title, t.due_date] for t in tasks]
    print(tabulate(rows, headers=["ID", "Title", "Due Date"], tablefmt="fancy_grid"))

def main():
    while True:
        print("\n📋 TASKTRACK MENU")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. View Task")
        print("4. Mark Task as Complete")
        print("5. Delete Task")
        print("6. View Upcoming Tasks")
        print("0. Exit")

        choice = input("Enter your choice: ")

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
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
