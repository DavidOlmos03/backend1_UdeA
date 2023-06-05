from fastapi import APIRouter
from connection.connection import session,database,Session
from schema.product_schema import productSchema
from model.product import product_model
from fastapi.exceptions import HTTPException


product = APIRouter()

                            ###***CRUD TABLE PRODUCTO***###
                    
@product.post("/api/Create_product", tags=["CrudProduct"])
def create_product(data_product: productSchema):
    existing_product = session.query(product_model).filter_by(id=data_product.id).first()
    #Es necesario implementar un try-except????
    if existing_product:
        session.commit()
        raise HTTPException(status_code=400, detail="El ID del producto ya existe")
    
    new_product = product_model(id = data_product.id, nombre=data_product.nombre, precio = data_product.precio, url_de_imagen=data_product.url_de_imagen)
    session.add(new_product)
    session.commit()
    session.refresh(new_product)   
    return new_product

@product.get("/api/check_id/{id}", tags = ["CrudProduct"])
async def check_id_exists(id: int):
    db = session
    
    obj_db = db.query(product_model).filter(product_model.id == id).first()
    #query = db.select().where(db.c.id == id)
    return obj_db 

@product.get("/api/read_product/{product_id}", tags=["CrudProduct"])
def get_product(id: int):
    result = session.query(product_model).get(id)
    return result


@product.put("/api/update_product/{product_id}", tags=["CrudProduct"])
def update_product(data_update: productSchema , product_id: int):
    db_product = session.query(product_model).filter(product_model.id == product_id).first()
    if db_product:
        # Actualiza los atributos del usuario con los valores proporcionados en usuario_actualizado
        for key, value in data_update.dict().items():
            setattr(db_product, key, value)
        session.commit()
        session.refresh(db_product)
        return {"message": "Product updated successfully"}


@product.delete("/api/delete_product/{product_id}", tags=["CrudProduct"])
def delete_product(product_id: int):
    db_product = session.query(product_model).filter(product_model.id == product_id).first()

    if db_product:
        session.delete(db_product)
        session.commit()
        return {"message": "Product deleted successfully"}
