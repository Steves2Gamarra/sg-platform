from app import db
from app.models import Recurso, Chamado, Usuario
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash


class RecursoService:

    @staticmethod
    def listar():

        return [

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
                "Controle de receitas, despesas e fluxo de caixa."
            )

        ]


class ChamadoService:

    @staticmethod
    def cadastrar(titulo, categoria, equipamento, descricao):

        ultimo = Chamado.query.order_by(
            Chamado.numero.desc()
        ).first()

        if ultimo:
            proximo = int(ultimo.numero[3:]) + 1
        else:
            proximo = 1

        numero = f"CH-{proximo:04d}"

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

        db.session.add(chamado)
        db.session.commit()


    @staticmethod
    def listar():

        return Chamado.query.order_by(
            Chamado.numero
        ).all()


    @staticmethod
    def buscar_por_numero(numero):

        numero_formatado = f"CH-{numero:04d}"

        return Chamado.query.filter_by(
            numero=numero_formatado
        ).first()


    @staticmethod
    def atualizar(
        numero,
        titulo,
        categoria,
        equipamento,
        descricao
    ):

        chamado = ChamadoService.buscar_por_numero(numero)

        if chamado is None:
            return

        chamado.titulo = titulo
        chamado.categoria = categoria
        chamado.equipamento = equipamento
        chamado.descricao = descricao

        db.session.commit()


    @staticmethod
    def excluir(numero):

        chamado = ChamadoService.buscar_por_numero(numero)

        if chamado is None:
            return

        db.session.delete(chamado)
        db.session.commit()


class UsuarioService:

    @staticmethod
    def buscar_por_email(email):

        return Usuario.query.filter_by(
            email=email
        ).first()


    @staticmethod
    def autenticar(email, senha):

        usuario = UsuarioService.buscar_por_email(email)

        if usuario is None:
            return None

        if not usuario.ativo:
            return None

        if not check_password_hash(usuario.senha, senha):
            return None

        return usuario


    @staticmethod
    def listar():

        return Usuario.query.order_by(
            Usuario.nome
        ).all()


    @staticmethod
    def buscar_por_id(id):

        return Usuario.query.get(id)


    @staticmethod
    def cadastrar(
        nome,
        email,
        senha,
        perfil,
        ativo=True
    ):

        usuario = Usuario(

            nome=nome,
            email=email,
            senha=generate_password_hash(senha),
            perfil=perfil,
            ativo=ativo

        )

        db.session.add(usuario)

        db.session.commit()

        return usuario