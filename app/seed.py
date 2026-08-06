from app import db
from app.models import Chamado

def criar_dados_iniciais():

    # Se já existem chamados, não faz nada
    if Chamado.query.first():

        return
    
    chamados = [

        Chamado(

            "CH-0001",
            "Servidor indisponível",
            "Hardware",
            "Servidor Principal",
            "Servidor indisponível desde às 08:00.",
            "Aberto",
            "Alta",
            "Carlos Silva",
            "30/07/2026 08:00"

        ),

        Chamado(

            "CH-0002",
            "Erro ao acessar o e-mail",
            "Software",
            "Notebook Dell Latitude",
            "Usuário não consegue acessar o Outlook",
            "Em andamento",
            "Média",
            "Ana Souza",
            "30/07/2026 09:15"

        ),

        Chamado(

            "CH-0003",
            "Instalação do Office",
            "Software",
            "Notebook Lenovo",
            "Solicitação de instalação do Microsoft Office.",
            "Concluído",
            "Baixa",
            "João Pereira",
            "29/07/2026 15:30"

        )

    ]

    db.session.add_all(chamados)

    db.session.commit()

