from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from utils.db import engine

Base = declarative_base()


class Ventas(Base):
    __tablename__ = 'Ventas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime)
    cedula = Column(String(10), nullable=False)
    cliente_name = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    telefono = Column(String(15), nullable=False)
    correo = Column(String(70), nullable=False)
    costo = Column(Float, nullable=False)
    metodo_pago = Column(Integer, nullable=False)
    estado_pedido = Column(Integer, nullable=False)

    def __init__(self, fecha, cedula, cliente_name, direccion, telefono, correo, costo, metodo_pago, estado_pedido):
        self.fecha = fecha
        self.cedula = cedula
        self.cliente_name = cliente_name
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.costo = costo
        self.metodo_pago = metodo_pago
        self.estado_pedido = estado_pedido
