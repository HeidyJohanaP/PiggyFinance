from typing import Dict
from pydantic import BaseModel

class Categoria(BaseModel):
    id: int
    nombre: str
    Descripcion: str

    