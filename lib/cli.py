from main import list_tasks, add_task, view_task, complete_task, delete_task, upcoming_tasks

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