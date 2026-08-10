from flask import Flask
from database.connection import db, ma, Config
from flask_marshmallow import Marshmallow
from views import category_router, user_router, product_router, registration_router

# define marshmallow
ma = Marshmallow()

def create_app():
    # create app
    app = Flask(__name__)

    # define routes
    app.register_blueprint(user_router, url_prefix="/user")
    app.register_blueprint(category_router, url_prefix="/category")
    app.register_blueprint(product_router, url_prefix="/product")
    app.register_blueprint(registration_router, url_prefix="/registration")

    # get URL from object Config
    app.config.from_object(Config)

    # create db in app
    db.init_app(app)

    # create marshmallow in app
    ma.init_app(app)

    return app