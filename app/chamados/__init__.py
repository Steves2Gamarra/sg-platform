from flask import Blueprint

chamados_bp = Blueprint(

    "chamados",

    __name__

)

from . import routes