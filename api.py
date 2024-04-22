from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from database.models.tallerista import Tallerista
from typing import List

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

@app.get('/talleristas/', response_model=List[Tallerista])
async def get_talleristas():
    talleristas = await db['talleristas'].find().to_list(128)
    return talleristas

@app.post('/verificar-tallerista/', response_model=Tallerista)
async def verificar_tallerista(tallerista: Tallerista):
    tallerista = await db['talleristas'].find_one_and_update({'enlace': tallerista.enlace}, {'$set': {'verificado': not tallerista.verificado}}, return_document=True)
    return tallerista
