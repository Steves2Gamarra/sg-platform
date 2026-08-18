from flask import render_template, request, redirect, url_for, session

from . import auth_bp

from app.services import UsuarioService


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        senha = request.form.get("senha")

        usuario = UsuarioService.autenticar(
            email,
            senha
        )

        if usuario is None:

            return render_template(
                "login.html",
                erro="E-mail ou senha inválidos."
            )

        session["usuario_id"] = usuario.id
        session["usuario_nome"] = usuario.nome
        session["usuario_perfil"] = usuario.perfil

        return redirect(url_for("chamados.home"))

    return render_template("login.html")

@auth_bp.route("/logout")

def logout():

    session.clear()

    return redirect(url_for("auth.login"))