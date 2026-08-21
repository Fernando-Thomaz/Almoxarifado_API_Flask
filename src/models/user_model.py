from sqlalchemy import Column, Integer, String
from src.database.connection import db
from passlib.context import CryptContext

class UserModel(db.Model):
    __tablename__ = "user"

    user_id = db.Column("user_id", Integer, primary_key=True, autoincrement=True)
    user_name = db.Column("user_name", String(120), nullable=False)
    user_email = db.Column("user_email", String(120), nullable=False, unique=True)
    user_password = db.Column("user_password", String(255), nullable=False)

    # set cryptocontext
    pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

    # hash password
    def gen_password(self, user_password):
        self.user_password = self.pwd_context.hash(user_password)

    # verify password
    def ver_password(self, user_password):
        return self.pwd_context.verify(user_password, self.user_password)