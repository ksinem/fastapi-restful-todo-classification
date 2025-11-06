
from sqlalchemy import Column, Integer, String, Text, Date, Enum
from database.db_session import Base
from model.enums import TodoState



class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer,primary_key=True)
    task = Column(String(100),nullable=False)
    description = Column(Text)
    deadline = Column(Date)
    state = Column(Enum(TodoState),nullable=False,default="OPEN")
    category = Column(Text, nullable=True)