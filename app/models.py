from app import db

class Recurso:

    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao


class Chamado(db.Model):

    __tablename__ = "chamados"

    numero = db.Column(db.String(10), primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    equipamento = db.Column(db.String(150))
    descricao = db.Column(db.Text)
    status = db.Column(db.String(30))
    prioridade = db.Column(db.String(30))
    responsavel = db.Column(db.String(100))
    data_abertura = db.Column(db.String(30))

    def __init__(
        self,
        numero,
        titulo,
        categoria,
        equipamento,
        descricao,
        status,
        prioridade,
        responsavel,
        data_abertura
    ):

        self.numero = numero
        self.titulo = titulo
        self.categoria = categoria
        self.equipamento = equipamento
        self.descricao = descricao
        self.status = status
        self.prioridade = prioridade
        self.responsavel = responsavel
        self.data_abertura = data_abertura

class Usuario(db.Model):

    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    senha = db.Column(db.String(255), nullable=False)

    perfil = db.Column(db.String(30), nullable=False)

    ativo = db.Column(db.Boolean, default=True)

   
        