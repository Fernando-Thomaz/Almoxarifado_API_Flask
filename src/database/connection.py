import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# carrega variaveis de ambiente
load_dotenv()

# defini o banco
db = SQLAlchemy()

# cria uma class de config para chamar a classe e nao o arquivo inteiro
class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv("URL_DATABASE")

    # desabilita o rastreamento de modificao dos objetos
    SQLALCHEMY_TRECK_MODIFICATIONS = False