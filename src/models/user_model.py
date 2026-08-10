from sqlalchemy import Column, Integer, String
from database.connection import db
from passlib.context import CryptoContext

class UserModel(db.Model):
    __tablename__ = "user"

    user_id = db.Column("user_id", Integer, primary_key=True, autoincrement=True)
    user_name = db.Column("user_name", String(120), nullable=False)
    user_email = db.Column("user_email", String(120), nullable=False, unique=True)
    user_password = db.Column("user_password", String(255), nullable=False)

    # set cryptocontext
    pwd_context = CryptoContext(schemes=["argon2"], deprecated="auto")

    # hash password
    def gen_password(self, user_password):
        self.user_password = self.pwd_context.hash(user_password)

    # verify password
    def ver_password(self, user_password):
        return self.pwd_context.verify(user_password, self.user_password)

    def __init__(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password