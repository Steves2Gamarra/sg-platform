from flask import render_template, request, redirect, url_for

from . import chamados_bp
from app.services import RecursoService, ChamadoService


@chamados_bp.route("/")
def home():

    recursos = RecursoService.listar()

    return render_template(
        "home.html",
        recursos=recursos
    )


@chamados_bp.route("/chamados")
def chamados():

    chamados = ChamadoService.listar()

    return render_template(
        "chamados.html",
        chamados=chamados
    )


@chamados_bp.route("/chamados/<int:id>")
def visualizar_chamado(id):

    chamado = ChamadoService.buscar_por_numero(id)

    if chamado is None:
        return "Chamado não encontrado", 404

    return render_template(
        "chamado_detalhes.html",
        chamado=chamado
    )


@chamados_bp.route("/chamados/<int:id>/editar")
def editar_chamado(id):

    chamado = ChamadoService.buscar_por_numero(id)

    if chamado is None:
        return "Chamado não encontrado", 404

    return render_template(
        "novo_chamado.html",
        chamado=chamado,
        titulo_pagina="Editar Chamado",
        texto_botao="Salvar Alterações"
    )


@chamados_bp.route("/chamados/<int:id>/editar", methods=["POST"])
def salvar_edicao(id):

    titulo = request.form.get("titulo")
    categoria = request.form.get("categoria")
    equipamento = request.form.get("equipamento")
    descricao = request.form.get("descricao")

    ChamadoService.atualizar(
        id,
        titulo,
        categoria,
        equipamento,
        descricao
    )

    return redirect(url_for("chamados.chamados"))


@chamados_bp.route("/chamados/<int:id>/excluir", methods=["POST"])
def excluir_chamado(id):

    ChamadoService.excluir(id)

    return redirect(url_for("chamados.chamados"))


@chamados_bp.route("/chamados/novo", methods=["GET", "POST"])
def novo_chamado():

    if request.method == "POST":

        titulo = request.form.get("titulo")
        categoria = request.form.get("categoria")
        equipamento = request.form.get("equipamento")
        descricao = request.form.get("descricao")

        ChamadoService.cadastrar(
            titulo,
            categoria,
            equipamento,
            descricao
        )

        return redirect(url_for("chamados.chamados"))

    return render_template(
        "novo_chamado.html",
        chamado=None,
        titulo_pagina="Novo Chamado",
        texto_botao="Abrir Chamado"
    )


    

       
    