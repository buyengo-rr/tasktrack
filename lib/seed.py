from models import Base, engine, session, Task
from datetime import date

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

tasks = [
    Task(title="Finish report", description="Complete the monthly sales report", due_date=date(2025, 6, 4)),
    Task(title="Workout", description="Go for a 30-minute run", due_date=date(2025, 6, 3)),
    Task(title="Call Mom", description="Check in and say hi", due_date=date(2025, 6, 3)),
    Task(title="Team Meeting", description="Weekly sync with project team", due_date=date(2025, 6, 5)),
]

session.add_all(tasks)
session.commit()

print("🌱 Seeding complete with sample tasks.")
