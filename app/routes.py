from flask import render_template
from app import app


@app.route("/")
def home():

    recursos = [

        recurso("chamados", "gerencie solicitaçõs."),
        recurso("inventario", "controle computadores")

    ]
    {
            "titulo": "Inventário",
            "descricao": "Controle computadores, notebooks e ativos."
        },

    {
            "titulo": "Usuários",
            "descricao": "Cadastre colaboradores e acompanhe acessos."
        },

    {
            "titulo": "Relatórios",
            "descricao": "Visualize indicadores e desempenho da equipe."
        },

    {
            "titulo": "Financeiro",
            "descricao": "Controle receitas, despesas e fluxo de caixa."
        }

    

    return render_template(
        "index.html",
        recursos=recursos
    )