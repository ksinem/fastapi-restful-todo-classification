from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_session import get_db
from database.crud import TodoRepository
from fast.schemas import TodoBase,TodoCreate,TodoRead, TodoDelete, TodoCategory
from model.table import Todo
from model.predict import predict_category


todo_router = APIRouter(prefix="/todos", tags=["todos"])

# ===== TODOS ==============================================================


@todo_router.post("/", response_model=TodoCategory)  #http://127.0.0.1:8000/todos/?user_id=1
def automatically_categorize_new_todo(todo:TodoCreate, db: Session = Depends(get_db)):
    repo = TodoRepository(db)
    predicted_category = predict_category(
        task=todo.task,
        description=todo.description if todo.description is not None else ""
    )
    todo_data = todo.model_dump()
    todo_data['category'] = predicted_category
    todo_db = Todo(**todo_data)
    return repo.create_todo(todo_db)

@todo_router.delete("/{todo_id}", response_model=bool)
def delete_todo(todo: TodoDelete, db:Session = Depends(get_db)):
    repo = TodoRepository(db)
    todo_db = Todo(**todo.model_dump())
    return repo.delete_todo(todo_db)




