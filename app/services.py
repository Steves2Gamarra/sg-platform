from app.models import Recurso

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