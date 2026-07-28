class Recurso:

    def __init__(self, titulo, descricao):

        self.titulo = titulo

        self.descricao = descricao

class Chamado:

    def __init__(
        self,
        numero,
        titulo,
        status,
        prioridade,
        responsavel
    ):

        self.numero = numero
        self.titulo = titulo
        self.status = status
        self.prioridade = prioridade
        self.responsavel = responsavel

@property
def status_css(self):

    if self.status == "Aberto":
        return "badge-open"

    if self.status == "Em andamento":
        return "badge-progress"

    return "badge-closed"

@property
def prioridade_css(self):

    if self.prioridade == "Alta":
        return "bafge-high"

    if self.prioridade == "Média":
        return "badge-medium"

    return "baf=dge-low"