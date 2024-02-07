from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import service, model, schema
from .database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todos", response_model=list[schema.ToDoItem])
def read_todos(db: Session = Depends(get_db)):
    todos = service.get_toDoItems(db)
    return todos

@app.post("/todos", response_model=schema.ToDoItem)
def create_todo(toDoItem: schema.ToDoCreate, db: Session = Depends(get_db)):
    return service.create_toDoItem(db, toDoItem)

@app.patch("/todos/{todo_id}", response_model=schema.ToDoItem)
def update_todo(todo_id: str, toDoItem: schema.ToDoItemUpdate, db: Session = Depends(get_db)):
    return service.update_toDoItem(db, int(todo_id), toDoItem)

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str, db: Session = Depends(get_db)):
    return service.delete_toDoItem(db, int(todo_id))
