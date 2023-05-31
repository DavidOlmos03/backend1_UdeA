from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import sessionmaker

#from flask import Flask
#from flask_cors import CORS

#app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

# Resto de la configuración del servidor

#if __name__ == '__main__':
 #   app.run(port=8000)


engine = create_engine('mysql+mysqlconnector://root@localhost/p_trabajoudea')
meta_data = MetaData()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()




