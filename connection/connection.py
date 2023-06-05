from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import sessionmaker
from databases import Database
#from flask import Flask
#from flask_cors import CORS

#app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

# Resto de la configuración del servidor

#if __name__ == '__main__':
 #   app.run(port=8000)

url = "mysql+mysqlconnector://root@localhost/p_trabajoudea"
engine = create_engine(url)
meta_data = MetaData()
Base = declarative_base()
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine) #ESTUDIAR
session = Session()
database = Database(url)

#Esta función permite crear una session en la base de datos para poder hacer querys en ella
"""def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()

"""


