from . import db
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__: str = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True)
    password = Column(String(150))
    categories = db.relationship("Category")
    # La "N" es mayúscula por que hace referencia al nombre de la clase en Python
    notes = db.relationship("Note")


class Note(db.Model):
    __tablename__: str = "note"
    id = Column(Integer, primary_key=True)
    content = Column(String(1000))
    date = Column(DateTime(timezone=True), default=datetime.now)
    complete = Column(Boolean, default=False)
    important = Column(Boolean, default=False)
    details = Column(Text)
    expires = Column(DateTime(timezone=True))
    category_id = Column(Integer, ForeignKey("category.id"))
    # La "u" de "user.id" es minúscula por que hace referencia al nombre de la tabla en la base de datos
    user_id = Column(Integer, ForeignKey("user.id"))


class Category(db.Model):
    __tablename__: str = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    notes = db.relationship("Note")
    user_id = Column(Integer, ForeignKey("user.id"))
