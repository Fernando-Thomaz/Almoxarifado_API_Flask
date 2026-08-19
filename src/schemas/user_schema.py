from src import ma
from src.models import UserModel
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        fields = ("id", "name", "email", "password")

    id = fields.Int(attribute="user_id", dump_only=True)
    name = fields.String(attribute="user_name", required=True)
    email = fields.Email(attribute="user_email", required=True)
    password = fields.String(attribute="user_password", required=True)

userschema = UserSchema()
usersschema = UserSchema(many=True)