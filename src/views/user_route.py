from flask import Blueprint

user_router = Blueprint("user", __name__)

@user_router.get("/")
def home():
    return {"mensagem": "entrou na rota"}