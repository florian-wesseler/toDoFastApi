# schema.py
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

# Klassenobjekt Base für ein ToDo Item Read/Create
class ToDoItemBase(BaseModel):
    title: str
    description: Optional[str] = None

# Klassenobjekt für einen Request zum Erstellen eines ToDo Items
class ToDoCreate(ToDoItemBase):
    dueDate: Optional[datetime] = None

class ToDoItemUpdate(ToDoCreate):
    done: bool = False

# Klassenobjekt für ein ToDo Item
class ToDoItem(ToDoItemUpdate):
    id: int

    class Config:
        from_attributes=True

# # Klassenobjekt für einen Request zum Aktualisieren eines ToDo Items
# class ToDoUpdate(BaseModel):
#     title: Optional[str] = None
#     description: Optional[str] = None
#     done: Optional[bool] = None

# # Klassenobjekt für einen Response zum Anzeigen eines ToDo Items
# class ToDoResponse(BaseModel):
#     item: ToDoItem

# # Klassenobjekt für einen Response zum Anzeigen einer Liste von ToDo Items
# class ToDoListResponse(BaseModel):
#     items: List[ToDoItem]
