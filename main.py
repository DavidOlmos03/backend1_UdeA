from Router.router import user,product,compra
from fastapi import FastAPI

app = FastAPI()

app.include_router(product)
app.include_router(user)
app.include_router(compra)
"""
@app.post("/items/crear_tabla_python")
def create_table():
    cursor = connection.cursor()
    create_table_query = 
    CREATE TABLE  Compra(
        usuario_id PRIMARY KEY,
        producto_id VARCHAR(30),
        total_productos int
    )
    cursor.execute(create_table_query)     
    connection.commit()
    cursor.close()
    connection.close()
 """


