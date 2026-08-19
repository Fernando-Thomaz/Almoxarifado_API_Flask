from src import ma
from src.models import RegistrationModel
from marshmallow import fields
from .product_schema import ProductSchema

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

    id = fields.Int(attribute="regi_id", dump_only=True)
    dt = fields.DateTime(attribute="regi_dt", required=True)
    type = fields.Boolean(attribute="regi_type", required=True)

registrationschema = RegistrationSchema()
registrationsschema = RegistrationSchema(many=True)