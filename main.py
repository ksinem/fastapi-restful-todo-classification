from fastapi import FastAPI
from fast.routers import todo_router
from database.db_session import Base, engine
from model.table import Todo



Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todo_router)

@app.get("/")  # http://127.0.0.1:8000/
def get_root():
    return {
        "message": "Welcome. Please go to http://127.0.0.1:8000/docs to view more."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)
