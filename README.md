# Grupo 1 - Apprende Custom Search

Continuación del proyecto de Análisis y Diseño de Software 2023-2.

## Integrantes

- Gabriel Apablaza V.
- Diego Concha B.
- Andrés Saldias S.
- Myckoll Winchester M.

## Requerimientos

- Python 3.12
- MongoDB 7.0

MongoDB debe estar corriendo en el puerto 27017, y debe tener una base de datos llamada "apprende-custom-search" con una colección llamada "talleristas" y otra "propuestas". Sensible a mayúsculas.

## Instalación

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
.venv\Scripts\activate
```

```bash
py app.py
```

```bash
uvicorn api:app --reload
```
