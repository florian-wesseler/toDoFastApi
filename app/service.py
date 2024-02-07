from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import model, schema

def get_toDoItems(db: Session):
    return db.query(model.ToDo).all()

def create_toDoItem(db: Session, item: schema.ToDoCreate):
    db_item = model.ToDo(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_toDoItem(db: Session, toDo_id: int, item: schema.ToDoItem):
    db_item = db.get(model.ToDo, toDo_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Hero not found")
    todo_data = item.model_dump(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(db_item, key, value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_toDoItem(db: Session, toDo_id: int):
    db_item = db.get(model.ToDo, toDo_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Hero not found")
    db.delete(db_item)
    db.commit()
    return {"ok": True}