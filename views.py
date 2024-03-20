from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.get("/")
def index() -> str:
    return render_template("index.html")

@views.get("/talleristas")
def talleristas() -> str:
    return render_template("talleristas.html")

@views.get("/insumos")
def insumos() -> str:
    return render_template("insumos.html")

@views.get("/marcadores")
def marcadores() -> str:
    return render_template("marcadores.html")

@views.get("/ejemplo")
def ejemplo() -> str:
    return render_template("ejemplo.html")

@views.get("/404")
def not_found() -> str:
    return render_template("not_found.html")
