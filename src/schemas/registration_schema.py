from src import ma
from src.models import RegistrationModel
from marshmallow import fields
from .product_schema import ProductSchema

class RegistrationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RegistrationModel
        load_instance = True
        fields = ("id", "dt", "type", "product")
        include_fk = True

    id = fields.Int(attribute="regi_id", dump_only=True)
    dt = fields.DateTime(attribute="regi_dt", required=True)
    type = fields.Boolean(attribute="regi_type", required=True)

    product = fields.Int(attribute="fk_prod_id", required=True)

registrationschema = RegistrationSchema()
registrationsschema = RegistrationSchema(many=True)