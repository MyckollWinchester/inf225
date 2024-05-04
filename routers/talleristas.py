from database.client import db
# from database.models.tallerista import Tallerista
from fastapi import APIRouter
# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from pymongo.cursor import Cursor

router = APIRouter()

@router.get("/talleristas")
async def tallerista():
    return db["talleristas"].find()
