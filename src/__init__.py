from flask import Flask
from database.connection import db, ma, Config
from flask_marshmallow import Marshmallow
from flask_restful import Api

# define marshmallow
ma = Marshmallow()

# define api restful
api = Api()

from .models import UserModel, CategoryModel, ProductModel, RegistrationModel
from .views import UserList, UserResourceEmail, UserResource, ProductList, ProductResource, ProductResourceName, ProductResourceCategory, CategoryList, CategoryResource, RegistrationResourceType, RegistrationResourceProduct, RegistrationResourceDate, RegistrationResource, RegistrationList

def create_app():
    # create app
    app = Flask(__name__)

    # get URL from object Config
    app.config.from_object(Config)

    # create db in app
    db.init_app(app)

    # create marshmallow in app
    ma.init_app(app)

    # create api for flask restful
    api.init_app(app)

    return app