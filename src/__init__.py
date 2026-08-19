from flask import Flask
from .database.connection import Config, db
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flasgger import Swagger

# define marshmallow
ma = Marshmallow()

# define api restful
api = Api()

def create_app():
    # create app
    app = Flask(__name__)

    # get URL from object Config
    app.config.from_object(Config)

    # create db in app
    db.init_app(app)

    # create marshmallow in app
    ma.init_app(app)


    # import views
    from . import views  # noqa: F401

    # create api for flask restful
    api.init_app(app)
    
    # define swagger for api
    swagger = Swagger(
        app,
        config={
            # config header
            "headers": [],
            "specs": [
                {
                    # http://localhost:5012/apispec.json
                    "endpoint": "apispec",
                    "route": "/apispec.json",

                    # include routes
                    "rule_filter": lambda rule: True,

                    # include models
                    "model_filter": lambda tag: True,
                },
            ],
            "static_url_path": "/flasgger_static",
            "swagger_ui": True,
            "specs_route": "/docs",
        },
    )

    return app