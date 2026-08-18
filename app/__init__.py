from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config["SECRET_KEY"] = "sg-platform-dev-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sg_platform.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

migrate = Migrate(app, db)


from app.models import Chamado, Usuario


from app.chamados import chamados_bp
app.register_blueprint(chamados_bp)


from app.auth import auth_bp
app.register_blueprint(auth_bp)


from app.usuarios import usuarios_bp
app.register_blueprint(usuarios_bp)