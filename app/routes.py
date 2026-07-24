from flask import render_template

from app import app

from app.services import RecursoService

@app.route("/")
def home():

    recursos = RecursoService.listar()

    return render_template(
        "home.html",
        recursos=recursos
    )

@app.route("/chamados")
def chamados():

    return render_template("chamados.html")