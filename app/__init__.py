from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "sg-platform-dev-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sg_platform.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from app.models import Chamado, Usuario

from app.seed import criar_dados_iniciais

from flask_migrate import Migrate

migrate = Migrate(app, db)

with app.app_context():

    db.create_all()

    criar_dados_iniciais()

from app.chamados import chamados_bp

app.register_blueprint(chamados_bp)

from app.auth import auth_bp

app.register_blueprint(auth_bp)
