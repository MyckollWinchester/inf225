from flask import (
    Blueprint,
    render_template,
)

views = Blueprint(__name__, "views")

@views.get("/")
def index():
    return render_template("index.html")


@views.get("/404")
def not_found():
    return "404"

