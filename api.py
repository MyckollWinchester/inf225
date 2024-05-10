from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from database.models.tallerista import Tallerista
from database.models.propuesta import Propuesta
from database.scripts.web_scrapers import jumbo_search
from database.scripts.openai_api import description_filter
from database.scripts.google_api import google_custom_search
from database.scripts.validators import validate_propuesta_taller

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

@app.get("/buscar-tallerista/", response_model=list[dict])
async def buscar_tallerista(prompt: str) -> list[dict]:
    if not prompt:
        raise HTTPException(
            status_code=400,
            detail="Búsqueda vacía."
        )
    filtered_prompt = description_filter(prompt)
    return google_custom_search(filtered_prompt)

@app.get("/buscar-insumo/", response_model=list[dict])
async def buscar_insumo(prompt: str) -> list[dict]:
    if not prompt:
        raise HTTPException(
            status_code=400,
            detail="Búsqueda vacía."
        )
    return jumbo_search(prompt)

@app.post("/marcar-tallerista/", response_model=dict[str, int | str])
async def marcar_tallerista(tallerista: Tallerista) -> dict[str, str]:
    tallerista_db = await db["talleristas"].find_one({"enlace": tallerista.enlace})
    if tallerista_db:
        raise HTTPException(
            status_code=409,
            detail="Tallerista ya se encuentra en los marcadores."
        )
    tallerista = tallerista.model_dump()
    await db["talleristas"].insert_one(tallerista)
    return { "status": 200, "message": "Tallerista marcado." } 

@app.post("/desmarcar-tallerista/", response_model=dict[str, int | str])
async def desmarcar_tallerista(tallerista: Tallerista) -> dict[str, str]:
    tallerista_db = await db["talleristas"].find_one({"enlace": tallerista.enlace})
    if tallerista_db:
        tallerista = tallerista.model_dump()
        await db["talleristas"].delete_one(tallerista)
        return { "status": 200, "message": "Tallerista eliminado." } 
    else:
        raise HTTPException(
            status_code=409,
            detail="Tallerista no se encuentra en los marcadores."
        )

@app.get("/buscar-persona-en-db/")
async def buscar_persona_en_db(prompt: str):
    if not prompt:
        raise HTTPException(
            status_code=400,
            detail="Búsqueda vacía."
        )
    
    else:
        tallerista_db = await db["talleristas"].find_one({"enlace": prompt})
        #print(tallerista_db)
        if tallerista_db:
            #tallerista_db['_id'] = str(tallerista_db['_id'])
            return True

@app.post("/propuestas/")
async def propuestas(form: dict):
    if not validate_propuesta_taller(form):
        raise HTTPException(
            status_code=400,
            detail="Formulario inválido."
        )
    form["nombre_taller"] = form.pop("nombre-taller")
    propuesta = Propuesta(**form)
    await db["propuestas"].insert_one(propuesta.model_dump())
    return { "status": 200, "message": "Propuesta enviada." } 
