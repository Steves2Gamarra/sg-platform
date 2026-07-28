from flask import render_template

from app import app

from app.services import RecursoService, ChamadoService

@app.route("/")
def home():

    recursos = RecursoService.listar()

    return render_template(
        "home.html",
        recursos=recursos
    )

@app.route("/chamados")
def chamados():

    chamados = ChamadoService.listar()

    return render_template(
        "chamados.html",
        chamados=chamados
    )

@app.route("/chamados/<int:id>")
def visualizar_chamado(id):

    chamados = ChamadoService.listar()

    chamado = None

    for item in chamados:

        if item.numero == f"CH-{id:04d}":

            chamado = item
            break

    if chamado is None:

        return "Chamado não encontrado", 404

    return render_template(
        "chamado_detalhes.html",
        chamado=chamado
    )

@app.route("/chamdos/novos")
def novo_chamado():

    return render_template(
        "novo_chamado.html"
        
    )
