from sqlalchemy import MetaData
from connection.connection import connection

meta_data = MetaData()

""""
users = Table("Usuarios",meta_data,
                Column("id", Integer, primary_key=True),
                Column("Nombre",String(255), nullable = False),
                Column("email",String(255),nullable = False),
                Column("contraseña",String(255),nullable = False))
"""
