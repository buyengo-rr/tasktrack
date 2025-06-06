from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    due_date = Column(Date)
    completed = Column(Boolean, default=False)
    priority = Column(String, default="Medium")
    tags = Column(String)
    notes = Column(String)
    created_at = Column(DateTime, default=datetime.now)

engine = create_engine("sqlite:///tasks.db")
Session = sessionmaker(bind=engine)
session = Session()
