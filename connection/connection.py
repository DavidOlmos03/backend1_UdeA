from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root@localhost/p_trabajoudea')
meta_data = MetaData()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()




