import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
CX = os.getenv('CX')

class Tallerista:
    def __init__(self, nombre: str, linkedin: str, foto_perfil: str) -> None:
        self.nombre = nombre
        self.linkedin = linkedin
        self.foto_perfil = foto_perfil

def google_custom_search(consulta):
    servicio = build('customsearch', 'v1', developerKey=GOOGLE_API_KEY)
    respuesta_api = servicio.cse().list(q=consulta, cx=CX).execute()
    respuesta = []
    if 'items' in respuesta_api:
        for item in respuesta_api['items']:
            try:
                item['pagemap']['metatags'][0]['og:image']
            except:
                continue
            tallerista = Tallerista(
                nombre=item['title'],
                linkedin=item['link'],
                foto_perfil=item['pagemap']['metatags'][0]['og:image']
            )
            respuesta.append({
                'titulo': tallerista.nombre,
                'enlace': tallerista.linkedin,
                'foto_perfil': tallerista.foto_perfil
            })
    return respuesta
