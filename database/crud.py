from model.table import Todo
from sqlalchemy.orm import Session
from model.predict import predict_category


class TodoRepository:

    def __init__(self,session:Session):
        self.session = session

    def create_todo(self,todo:Todo) -> Todo:
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo

    def delete_todo_by_id(self, todo_id: int) -> bool:
        todo_to_delete = self.session.query(Todo).filter(Todo.id == todo_id).first()
        if todo_to_delete:
            self.session.delete(todo_to_delete)
            self.session.commit()
            return True
        return False

    def delete_todo_by_state(self, todo_state: str) -> bool:
        deleted_count = self.session.query(Todo).filter(Todo.state == todo_state).delete(synchronize_session='fetch')
        self.session.commit()
        return deleted_count > 0


    def predict_category(self, todo:Todo) -> str:
        predicted_cat = predict_category(todo.task, todo.description)
        todo.category = predicted_cat
        self.session.commit()
        self.session.refresh(todo)
        return predicted_cat


#