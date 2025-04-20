from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from utils.db import engine

Base = declarative_base()


class Usuarios(Base):
    __tablename__ = 'Usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(240), nullable=False)
    fullname = Column(String(50), nullable=False)
    rol = Column(String(20))
    fecha = Column(DateTime)
    deleted = Column(Boolean)

    def __init__(self, username, password, fullname, rol, fecha, deleted):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.rol = rol
        self.fecha = fecha
        self.deleted = deleted
