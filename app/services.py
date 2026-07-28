from app.models import Recurso, Chamado

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

    @staticmethod
    def listar():

        return [

            Chamado(          

                "CH-0001",
                "Servidor indisponível",
                "Aberto",
                "Alta",
                "Carlos silva"

            ),

            Chamado(  

                "CH-0002",
                "Erro ao acessar o e-mail",
                "Em andamneto",
                "Média",
                "Ana Souza"

            ),

            Chamado(

                "CH-0003",
                "Instalação do Oficce",
                "Concluído",
                "Baixa",
                "João Pereira"
            ) 

        ]