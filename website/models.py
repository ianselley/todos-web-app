from . import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    ForeignKey,
    Date,
)
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__: str = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True)
    password = Column(String(150))
    categories = db.relationship("Category")
    # The "N" is uppercase because it references the class name in python
    notes = db.relationship("Note")


class Note(db.Model):
    __tablename__: str = "note"
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    date = Column(DateTime(timezone=True), default=datetime.now)
    complete = Column(Boolean, default=False)
    important = Column(Boolean, default=False)
    details = Column(Text, default="")
    expires = Column(Date)
    category_id = Column(Integer, ForeignKey("category.id"))
    # The "u" in "user.id" is lowercase because it references the table name in the database
    user_id = Column(Integer, ForeignKey("user.id"))


class Category(db.Model):
    __tablename__: str = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    notes = db.relationship("Note")
    user_id = Column(Integer, ForeignKey("user.id"))
