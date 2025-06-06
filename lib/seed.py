from models import Base, engine, session, Task
from datetime import date, datetime

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

tasks = [
    Task(title="Finish report", description="Complete the monthly sales report", due_date=date(2025, 6, 4), priority="High", tags="Work,Finance", notes="Data from Q2 pending.", created_at=datetime(2025,6,1,9,0)),
    Task(title="Workout", description="Go for a 30-minute run", due_date=date(2025, 6, 3), priority="Medium", tags="Health,Fitness", notes="Try interval training.", created_at=datetime(2025,6,2,7,30)),
    Task(title="Call Mom", description="Check in and say hi", due_date=date(2025, 6, 3), priority="Low", tags="Personal,Family", notes="Share weekend plans.", created_at=datetime(2025,6,2,19,0)),
    Task(title="Team Meeting", description="Weekly sync with project team", due_date=date(2025, 6, 5), priority="Medium", tags="Work,Meetings", notes="Prepare sprint notes.", created_at=datetime(2025,6,3,10,0))
]

session.add_all(tasks)
session.commit()

print("🌱 Seeding complete with sample tasks.")
