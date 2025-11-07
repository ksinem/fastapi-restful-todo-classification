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
def add_and_categorize_new_todo(todo:TodoCreate, db: Session = Depends(get_db)):
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
def delete_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    repo = TodoRepository(db)
    was_deleted = repo.delete_todo_by_id(todo_id)
    if not was_deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return True


@todo_router.delete("/state/{todo_state}", response_model=bool)
def delete_todo_by_state(todo_state: str, db: Session = Depends(get_db)):
    repo = TodoRepository(db)
    was_deleted = repo.delete_todo_by_state(todo_state)
    if not was_deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return True


