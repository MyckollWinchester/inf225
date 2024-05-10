from typing import Optional
from pydantic import BaseModel


class Propuesta(BaseModel):
    nombre: str
    apellidos: str
    experiencia: str
    correo: str
    telefono: str
    linkedin: Optional[str]
    instagram: Optional[str]
    tiktok: Optional[str]
    nombre_taller: str
    descripcion: str
    modalidad: str
    materiales: Optional[str]
    vacantes: int
    sesiones: int
