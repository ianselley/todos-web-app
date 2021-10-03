from . import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from flask_login import UserMixin
# from sqlalchemy.sql import func
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True)
    password = Column(String(150))
    # La "N" es mayúscula por que hace referencia al nombre de la clase en Python
    notes = db.relationship('Note')


class Note(db.Model):
    __tablename__: str = 'note'
    # Automáticamente esta PK se convertirá en SERIAL (AUTOINCREMENT)
    id = Column(Integer, primary_key=True)
    content = Column(String(1000))
    # Si no funciona usar: func.now()
    date = Column(DateTime(timezone=True), default=datetime.now)
    complete = Column(Boolean, default=False)
    # La "u" es minúscula por que hace referencia al nombre de la tabla en la base de datos
    user_id = Column(Integer, ForeignKey('user.id'))
