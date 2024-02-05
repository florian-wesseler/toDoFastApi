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