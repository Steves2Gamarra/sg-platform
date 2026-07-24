from flask import render_template

from app import app

from app.services import RecursoService

@app.route("/")
def home():

    recursos = RecursoService.listar()

    return render_template(
        "index.html",
        recursos=recursos
    )