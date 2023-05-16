from fastapi import APIRouter
from connection.connection import connection
from schema.user_schema import UserSchema
from schema.product_schema import productSchema
from schema.compra_schema import compraSchema

user = APIRouter()
product = APIRouter()
compra = APIRouter()


"""""
@user.get("/api/read_users")
def get_users():
    cursor = connection.cursor()
    consulta = "SELECT * FROM usuarios"
    cursor.execute(consulta)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

    return result
"""

@user.post("/Create_user")
def create_user(user: UserSchema):
    cursor = connection.cursor()
    consulta = "INSERT INTO usuarios (id, nombre, email, contrase) VALUES (%s,%s,%s,%s)"
    valores = (user.id, user.nombre, user.email, user.contrase)
    cursor.execute(consulta, valores)

    connection.commit()
    cursor.close()
    connection.close()
    return {"mensaje": "Usuario creado exitosamente"}


@user.get("/api/read_user/{user_id}")
def get_user(id: int):
    cursor = connection.cursor()
    consulta = f"SELECT * FROM usuarios WHERE id = {id}"
    cursor.execute(consulta)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

    return result


@user.put("/api/update_users/{user_id}")
def update_user(data_update: UserSchema , user_id: int):
    cursor = connection.cursor()
    consulta = f"UPDATE usuarios SET nombre = '{data_update.nombre}', email = '{data_update.email}', contrase = '{data_update.contrase}' WHERE id = {user_id}"
    cursor.execute(consulta)
    connection.commit()
    cursor.close()
    connection.close()


@user.delete("/api/delete_user/{user_id}")
def delete_user(user_id: int):
    cursor = connection.cursor()
    consulta = f"DELETE FROM usuarios WHERE id = {user_id}"
    cursor.execute(consulta)
    connection.commit()
    cursor.close()
    connection.close()


####CRUD PRODUCTO
@product.post("/Create_product")
def create_product(product: productSchema):
    cursor = connection.cursor()
    consulta = "INSERT INTO producto (id, nombre, precio, url_de_imagen) VALUES (%s,%s,%s,%s)"
    valores = (product.id, product.nombre, product.precio, product.url_de_imagen)
    cursor.execute(consulta, valores)

    connection.commit()
    cursor.close()
    connection.close()
    return {"mensaje": "Producto creado exitosamente"}


@product.get("/api/read_product/{product_id}")
def get_product(id: int):
    cursor = connection.cursor()
    consulta = f"SELECT * FROM producto WHERE id = {id}"
    cursor.execute(consulta)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

    return result


@product.put("/api/update_product/{product_id}")
def update_product(data_update: productSchema , product_id: int):
    cursor = connection.cursor()
    consulta = f"UPDATE producto SET nombre = '{data_update.nombre}', precio = '{data_update.precio}', url_de_imagen = '{data_update.url_de_imagen}' WHERE id = {product_id}"
    cursor.execute(consulta)
    connection.commit()
    cursor.close()
    connection.close()


@product.delete("/api/delete_product/{product_id}")
def delete_product(product_id: int):
    cursor = connection.cursor()
    consulta = f"DELETE FROM producto WHERE id = {product_id}"
    cursor.execute(consulta)
    connection.commit()
    cursor.close()
    connection.close()

##WORKING WHITH COMPRA
@compra.put("/api/update_compra/{id_user}/{id_producto}/{total_productos}")
def update_compra(id_user: int, id_product: int,total_productos:int):
    cursor = connection.cursor()
    consulta = f"""INSERT INTO compra (usuario_id, producto_id, total_productos)
                    SELECT 
                        (SELECT id FROM usuarios WHERE id = {id_user}),
                        (SELECT id FROM producto WHERE id = {id_product}),
                        '{total_productos}';"""
    cursor.execute(consulta)
    connection.commit()
    cursor.close()
    connection.close()
