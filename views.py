from flask import Blueprint, render_template, redirect, url_for, request
from database.scripts.validators import validate_propuesta_taller
import requests

views = Blueprint(__name__, "views")

@views.get("/")
@views.get("/inicio")
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

@views.get("/propuesta-taller")
@views.post("/propuesta-taller")
def propuesta_taller() -> str:
    if request.method == "GET":
        return render_template("propuesta_taller.html")
    else:
        if validate_propuesta_taller(request.form):
            requests.post("http://127.0.0.1:8000/propuestas", json=request.form)
            return redirect(url_for("views.success"))
        else:
            return render_template("propuesta_taller.html", form=request.form)

@views.get("/success")
def success() -> str:
    return render_template("success.html")

@views.get("/404")
def not_found() -> str:
    return render_template("not_found.html")
