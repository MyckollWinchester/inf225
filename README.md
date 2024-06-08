# Grupo 1 - Apprende Custom Search

Continuación del proyecto de Análisis y Diseño de Software 2023-2.

## Video presentación - hito 4

https://youtu.be/3orKcFlz7tg

## Integrantes

- Gabriel Apablaza V.
- Diego Concha B.
- Andrés Saldias S.
- Myckoll Winchester M.

## Requerimientos

- Python >3.12
- MongoDB >7.0

MongoDB debe estar corriendo en el puerto 27017 y debe tener una base de datos llamada `apprende-custom-search` con las colecciones: `talleres`, `propuestas` e `insumos`.

## API Keys

Se debe crear un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

```env
OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GOOGLE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
CX="xxxxxxxxxxxxxxxxx"
```

Los enlaces respectivos para obtener las keys son:

- [OpenAI](https://platform.openai.com/api-keys)
- [Google](https://developers.google.com/custom-search/v1/overview?hl=es-419#api_key)
- [Custom Search Engine](https://programmablesearchengine.google.com/controlpanel/create)

Donde `CX (Custom Search Engine)` debe tener la siguiente configuración:

![Configuración del CX](/static/img/readme/cx-config.png)

## Instalación

Crear un entorno virtual e instalar las dependencias

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

Activar el entorno virtual

```bash
.venv\Scripts\activate
```

En una terminal, ejecutar la API de la aplicación

```bash
uvicorn api:app --reload
```

En otra terminal, ejecutar la aplicación

```bash
py app.py
```

