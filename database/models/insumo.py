from pydantic import BaseModel


class Insumo(BaseModel):
    nombre: str
    enlace: str
    precio: str
    foto: str
