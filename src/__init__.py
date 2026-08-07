from flask import Flask
from database.connection import db, ma, Config
from flask_marshmallow import Marshmallow

# define marshmallow
ma = Marshmallow()

def create_app():
    # create app
    app = Flask(__name__)

    # get URL from object Config
    app.config.from_object(Config)

    # create db in app
    db.init_app(app)

    # create marshmallow in app
    ma.init_app(app)

    # route
    @app.get("/")
    def home():
        return {"mensagem": "funcionando"}, 200

    return app