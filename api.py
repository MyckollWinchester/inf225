from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from database.models.tallerista import Tallerista
from database.scripts.web_scrapers import jumbo_search

app = FastAPI()
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["apprende-custom-search"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/talleristas/", response_model=list[Tallerista])
async def get_talleristas() -> list[Tallerista]:
    return await db["talleristas"].find().to_list(128)

@app.post("/verificar-tallerista/", response_model=Tallerista)
async def verificar_tallerista(tallerista: Tallerista) -> Tallerista:
    return await db["talleristas"].find_one_and_update(
        {"enlace": tallerista.enlace},
        {"$set": {"verificado": not tallerista.verificado}},
        return_document=True
    )

@app.get("/buscar-insumo/", response_model=list[dict])
async def buscar_insumo(prompt: str) -> list[dict]:
    if not prompt:
        raise HTTPException(
            status_code=400,
            detail="Búsqueda vacía."
        )
    return jumbo_search(prompt)
