from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import Generator
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "todolist_categorized.db"
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"


engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db() -> Generator[Session,None,None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# class MySession(Session):
#
#     def __init__(self, database_url: str):
#         super().__init__()
#         self.database_url = database_url
#         engine = create_engine(self.database_url, echo=True)
#         self.Session = sessionmaker(bind=engine)
#         self.Base = declarative_base()
#
#     def get_db(self) -> Generator[Session, None, None]:
#         db = self.Session()
#         try:
#             yield db
#         finally:
#             db.close()


