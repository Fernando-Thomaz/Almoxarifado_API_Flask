from src import ma
from src.models import UserModel
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        fields = ("id", "name", "email", "password")

    name = fields.String(required=True)
    email = fields.Email(required=True)
    senha = fields.String(required=True)

user_schema = UserSchema(many=True)