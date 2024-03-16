from flask import Flask, redirect, url_for
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")


@app.errorhandler(404)
def not_found(e):
    return redirect(url_for("views.not_found"))


if __name__ == "__main__":
    app.run(debug=True, port=3030)
