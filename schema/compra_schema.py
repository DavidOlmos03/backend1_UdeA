from pydantic import BaseModel
from typing import Optional

class compraSchema(BaseModel):
    usuario_id: Optional[int]
    producto_id: Optional[int]
    total_productos: int  