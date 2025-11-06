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

    def delete_todo(self, todo:Todo) -> Todo:
        self.session.delete(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo

    def predict_category(self, todo:Todo) -> str:
        predicted_cat = predict_category(todo.task, todo.description)
        todo.category = predicted_cat
        self.session.commit()
        self.session.refresh(todo)
        return predicted_cat


#