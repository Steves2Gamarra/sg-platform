from flask import render_template, request, redirect, url_for

from . import usuarios_bp
from app.auth.decorators import role_required
from app.services import UsuarioService


@usuarios_bp.route("/usuarios")
@role_required("admin")
def usuarios():

    usuarios = UsuarioService.listar()

    return render_template(
        "usuarios.html",
        usuarios=usuarios
    )


@usuarios_bp.route(
    "/usuarios/novo",
    methods=["GET", "POST"]
)
@role_required("admin")
def novo_usuario():

    if request.method == "POST":

        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        perfil = request.form.get("perfil")
        ativo = request.form.get("ativo") == "on"

        UsuarioService.cadastrar(
            nome,
            email,
            senha,
            perfil,
            ativo
        )

        return redirect(
            url_for("usuarios.usuarios")
        )

    return render_template(
        "novo_usuario.html"
    )




