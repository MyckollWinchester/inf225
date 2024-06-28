import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def description_filter(prompt: str) -> str:
    """
    # No se puede utilizar la API de OpenAI
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": f'Como organizador de talleres, le proporcionaré la descripción de un taller a realizar, y será su trabajo traducir el prompt a algo que Google pueda entender. Lo que se busca es encontrar a potenciales talleristas para la realización del taller. Solo me tienes que responder con la búsqueda de Google (y sin usar comillas, ya que sino sería una búsqueda exacta), nada de texto extra ya que será automatizado, solo rescatar la información de temática del taller y la ubicación del taller (si es que se especifica). La temática del taller sí o sí debe ser especificada, si la temática del taller no es explícita, responder de la siguiente manera:\n"[error] No es clara la temática taller, no puedo buscar talleristas."\nTambién usar palabras clave como "Tallerista", "profesor" y evitar las como "taller" o "curso", ya que google podría buscar otro talleres en lugar de personas que es lo que nos interesa.\nMi primera solicitud es «{prompt}». Ignorar cualquier información que no sea la temática del taller y la ubicación del taller. También, no olvidar responder con "[error] No es clara la temática taller, no puedo buscar talleristas." en caso de ser necesario.',
        }],
        max_tokens=32,
    ).choices[0].message.content
    """
    return prompt

if __name__ == "__main__":
    prompt = "Voy a realizar un taller de pintura al óleo, asistirán aproximadamente 20 personas de manera presencial, cerca de quinta normal"
    response = description_filter(prompt)
    print(response)
