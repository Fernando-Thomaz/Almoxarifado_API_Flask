import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# load envirements
load_dotenv()

# define db
db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv("URL_DATABASE")

    # desable tracking the object
    SQLALCHEMY_TRECK_MODIFICATIONS = False