from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, create_engine, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
Base = declarative_base()
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, default="")
    due_date = Column(Date)
    priority = Column(String(20), default="Medium")  # e.g. Low, Medium, High, Critical
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    completed = Column(Boolean, default=False)
