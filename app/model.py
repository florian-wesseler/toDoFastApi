# model.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

# Erstelle eine Klasse für die User-Tabelle
# class User(Base):
#     __tablename__ = "user"

#     # Definiere die Spalten der Tabelle
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     email = Column(String, unique=True, nullable=False)
#     password = Column(String, nullable=False)

#     # Definiere eine Beziehung zu der ToDo-Tabelle
#     todos = relationship("ToDo", back_populates="user")

#     # Definiere eine Repräsentationsmethode für die Klasse
#     def __repr__(self):
#         return f"<User(id={self.id}, name={self.name}, email={self.email})>"

# Erstelle eine Klasse für die ToDo-Tabelle
class ToDo(Base):
    __tablename__ = "todo"

    # Definiere die Spalten der Tabelle
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    done = Column(Boolean, default=False)
    dueDate = Column(DateTime)

    # Definiere eine Fremdschlüsselbeziehung zu der User-Tabelle
    # user_id = Column(Integer, ForeignKey("user.id"))

    # Definiere eine Beziehung zu der User-Klasse
    # user = relationship("User", back_populates="todos")

    # Definiere eine Repräsentationsmethode für die Klasse
    # def __repr__(self):
    #     return f"<ToDo(id={self.id}, title={self.title}, done={self.done})>"
