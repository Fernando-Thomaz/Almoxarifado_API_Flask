from flask import Flask
from database.connection import db, Config

def create_app():
    # cria o app
    app = Flask(__name__)

    # pega a url do banco do objeto Config
    app.config.from_object(Config)

    # cria o banco dentro do app
    db.init_app(app)

    @app.get("/")
    def home():
        return {"mensagem": "funcionando"}, 200

    return app