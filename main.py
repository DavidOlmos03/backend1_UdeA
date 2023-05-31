from Router.userRouter import user
from Router.productRouter import product
from Router.router import compra
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.include_router(user)
app.include_router(product)
app.include_router(compra)
# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:4200",
    "http://localhost:8000/docs",
    "http://localhost:8000/docs#/CrudProduct/create_product",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



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


