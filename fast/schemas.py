from pydantic import BaseModel,Field,ConfigDict
from datetime import date
from model.enums import TodoState

class TodoBase(BaseModel):
    task:str
    description:str | None = None
    deadline:date | None = None
    state:TodoState = TodoState.OPEN

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class TodoDelete(TodoBase):
    task:str

class TodoCreate2(TodoBase):
    task: str
    description: str

