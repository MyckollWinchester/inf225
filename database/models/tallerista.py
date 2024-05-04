from pydantic import BaseModel


class Tallerista(BaseModel):
    titulo: str
    enlace: str
    verificado: bool
    foto_perfil: str
