from fastapi import APIRouter
from connection.connection import engine,session
from schema.user_schema import UserSchema
from schema.product_schema import productSchema
from schema.compra_schema import compraSchema
from model.user import user_model
from model.product import product_model
from typing import List


product = APIRouter()
user = APIRouter()
compra = APIRouter()

                            ###***CRUD TABLE USUARIOS***###
"""
@user.get("/api/show_table_usuarios")
def get_users():
    result =  session.query(user_model).all()
    return jsonable_encoder(result)

"""                            

@user.post("/api/Create_new_user")
def create_user(data_user: UserSchema):
    new_user = user_model(id = data_user.id, nombre=data_user.nombre, email=data_user.email, contrase=data_user.contrase)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)   
    return new_user

@user.get("/api/read_user")
def get_users(id: int):
    result = session.query(user_model).get(id)
    return result


@user.put("/api/update_users/{user_id}")
def update_user(data_update: UserSchema , user_id: int):
        db_usuario = session.query(user_model).filter(user_model.id == user_id).first()
        if db_usuario:
            # Actualiza los atributos del usuario con los valores proporcionados en usuario_actualizado
            for key, value in data_update.dict().items():
                setattr(db_usuario, key, value)
            session.commit()
            session.refresh(db_usuario)
            return {"message": "User updated successfully"}


@user.delete("/api/delete_user/{user_id}")
def delete_user(user_id: int):
    db_usuario = session.query(user_model).filter(user_model.id == user_id).first()

    if db_usuario:
        session.delete(db_usuario)
        session.commit()
        return {"message": "User deleted successfully"}


                            ###***CRUD TABLE PRODUCTO***###
@product.post("/Create_product")
def create_product(data_product: productSchema):
    new_product = product_model(id = data_product.id, nombre=data_product.nombre, precio = data_product.precio, url_de_imagen=data_product.url_de_imagen)
    session.add(new_product)
    session.commit()
    session.refresh(new_product)   
    return new_product

#############HERE
@product.get("/api/read_product/{product_id}")
def get_product(id: int):
    cursor = engine.cursor()
    consulta = f"SELECT * FROM producto WHERE id = {id}"
    cursor.execute(consulta)
    result = cursor.fetchall()
    engine.commit()
    cursor.close()
    engine.close()

    return result


@product.put("/api/update_product/{product_id}")
def update_product(data_update: productSchema , product_id: int):
    cursor = engine.cursor()
    consulta = f"UPDATE producto SET nombre = '{data_update.nombre}', precio = '{data_update.precio}', url_de_imagen = '{data_update.url_de_imagen}' WHERE id = {product_id}"
    cursor.execute(consulta)
    engine.commit()
    cursor.close()
    engine.close()


@product.delete("/api/delete_product/{product_id}")
def delete_product(product_id: int):
    cursor = engine.cursor()
    consulta = f"DELETE FROM producto WHERE id = {product_id}"
    cursor.execute(consulta)
    engine.commit()
    cursor.close()
    engine.close()

##WORKING WHITH COMPRA
@compra.put("/api/update_compra/{id_user}/{id_producto}/{total_productos}")
def update_compra(id_user: int, id_product: int,total_productos:int):
    cursor = engine.cursor()
    consulta = f"""INSERT INTO compra (usuario_id, producto_id, total_productos)
                    SELECT 
                        (SELECT id FROM usuarios WHERE id = {id_user}),
                        (SELECT id FROM producto WHERE id = {id_product}),
                        '{total_productos}';"""
    
    cursor.execute(consulta)
    engine.commit()
    cursor.close()
    engine.close()
