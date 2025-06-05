from sqlalchemy import Column, Integer, String, Boolean, Date, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    due_date = Column(Date)
    completed = Column(Boolean, default=False)

engine = create_engine("sqlite:///tasks.db")
Session = sessionmaker(bind=engine)
session = Session()
