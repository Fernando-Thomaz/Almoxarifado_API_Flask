from sqlalchemy import Column, Integer, String
from database.connection import db
from passlib.context import CryptoContext

class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column("user_id", Integer, primary_key=True, autoincrement=True)
    user_name = db.Column("user_name", String(120), nullable=False)
    user_email = db.Column("user_email", String(120), nullable=False, unique=True)
    user_senha = db.Column("user_senha", String(255), nullable=False)

    # set cryptocontext
    pwd_context = CryptoContext(schemes=["argon2"], deprecated="auto")

    # hash password
    def gen_senha(self, user_senha):
        self.user_senha = self.pwd_context.hash(user_senha)

    # verify password
    def ver_senha(self, user_senha):
        return self.pwd_context.verify(user_senha, self.user_senha)

    def __init__(self, user_name, user_email, user_senha):
        self.user_name = user_name
        self.user_email = user_email
        self.user_senha = user_senha