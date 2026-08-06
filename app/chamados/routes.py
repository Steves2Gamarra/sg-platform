from flask import render_template

from . import chamados_bp

@chamados_bp.route("/teste")

def teste():

    return "<h1>Blueprint funcionando!</h1>"