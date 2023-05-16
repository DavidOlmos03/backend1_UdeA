from pydantic import BaseModel
from typing import Optional

class productSchema(BaseModel):
    id: Optional[int]
    nombre: str
    precio: int
    url_de_imagen: str