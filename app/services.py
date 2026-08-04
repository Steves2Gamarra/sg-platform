from app.models import Recurso, Chamado
from datetime import datetime

class RecursoService:

    @staticmethod
    def listar():

        return [

            Recurso(
            
                "Chamados",
                "Gerencie solicitaçõs técnicas."
            
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
                "Visualize indicadores e desempenho da equipe"

            ),

            Recurso(

                "Financeiro",
                "Controle de receitas, despesas e fluxo de caixa"

            )

        ]

class ChamadoService:

    _chamados = [

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

    @staticmethod
    def cadastrar(titulo, categoria, equipamento, descricao):

        numero = f"CH-{len(ChamadoService._chamados) + 1:04d}"

        chamado = Chamado(

        numero,
        titulo,
        categoria,
        equipamento,
        descricao,
        "Aberto",
        "Média",
        "Fila de Atendimento",
        datetime.now().strftime("%d/%m/%Y %H:%M")

    )

        ChamadoService._chamados.append(chamado)

    @staticmethod
    def listar():

        return Chamado.query.order_by(Chamado.numero).all()

    @staticmethod
    def buscar_por_numero(numero):

        numero_formatado = f"CH-{numero:04d}"

        for chamado in ChamadoService._chamados:

            if chamado.numero == numero_formatado:

                return chamado
            
        return None

    @staticmethod
    def atualizar(numero, titulo, categoria, equipamento, descricao):

        chamado = ChamadoService.buscar_por_numero(numero)

        if chamado is None:

            return

        chamado.titulo = titulo
        chamado.categoria = categoria
        chamado.equipamento = equipamento
        chamado.descricao = descricao

    @staticmethod
    def excluir(numero):

        chamado = ChamadoService.buscar_por_numero(numero)

        if chamado is None:

            return

        ChamadoService._chamados.remove(chamado)


    
