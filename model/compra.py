from sqlalchemy import Column, Integer, ForeignKey
from connection.connection import Base
from sqlalchemy.orm import relationship
from connection.connection import engine
class compra_model(Base):
    __tablename__ = 'compras'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuarios.id'))
    product_id = Column(Integer , ForeignKey('productos.id'))
    total_products = Column(Integer, nullable=False)

    user = relationship("user_model")
    product = relationship("product_model")
