from app import db
from app.models import Chamado, Usuario
from werkzeug.security import generate_password_hash


def criar_dados_iniciais():

    # =========================
    # CHAMADOS
    # =========================

    if not Chamado.query.first():

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


    # =========================
    # USUÁRIO ADMINISTRADOR
    # =========================

    usuario = Usuario.query.filter_by(
        email="admin@sgplatform.local"
    ).first()

    if usuario is None:

        usuario = Usuario(
            nome="Administrador",
            email="admin@sgplatform.local",
            senha=generate_password_hash("Admin@123"),
            perfil="admin",
            ativo=True
        )

        db.session.add(usuario)


    db.session.commit()