from src import ma
from src.models import RegistrationModel
from marshmallow import fields
from src.schemas import ProductSchema

class RegistrationSchema(ma.SQLAlchemyAutoSchema):
    # foreign key
    product = fields.Nested(
        ProductSchema,
        dump_only=True
    )

    class Meta:
        model = RegistrationModel
        load_instance = True
        fields = ("id", "dt", "type")
        include_fk = True

    dt = fields.DateTime(required=True)
    type = fields.Boolean(required=True)

registration_schema = RegistrationSchema(many=True)