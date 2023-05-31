from fastapi import APIRouter
from connection.connection import session
from schema.product_schema import productSchema
from model.product import product_model

product = APIRouter()

                            ###***CRUD TABLE PRODUCTO***###
                    
@product.post("/api/Create_product", tags=["CrudProduct"])
def create_product(data_product: productSchema):
    new_product = product_model(id = data_product.id, nombre=data_product.nombre, precio = data_product.precio, url_de_imagen=data_product.url_de_imagen)
    session.add(new_product)
    session.commit()
    session.refresh(new_product)   
    return new_product


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
