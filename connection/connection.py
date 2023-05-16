import mysql.connector
from fastapi import FastAPI

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password = '', 
    database='p_trabajoudea'
)

app = FastAPI()

