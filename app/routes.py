from flask import render_template
from app import app
from app.models import Recurso


@app.route("/")
def home():

    recursos = [

        Recurso(
            "Chamados",
            "Gerencie solicitações técnicas."
        ),

        Recurso(
            "Inventário",
            "Controle computadores, notebooks e ativos."
        ),

        Recurso(
            "Usuários",
            "Cadastre colaboradores e acompanhe acessos."
        ),

        Recurso(
            "Relatórios",
            "Visualize indicadores e desempenho da equipe."
        ),

        Recurso(
            "Financeiro",
            "Controle receitas, despesas e fluxo de caixa."
        )

    ]

    return render_template(
        "index.html",
        recursos=recursos
    )