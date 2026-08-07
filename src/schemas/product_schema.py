from src import ma
from marshmallow import fields
from src.models import ProductModel
from src.schemas import CategorySchema

class ProductSchema(ma.SQLAlchemyAutoSchema):
    category = fields.Nested(
        CategorySchema,
        dump_only=True
    )

    class Meta:
        model = ProductModel
        load_instance = True
        fields = ("id", "name", "unit_measure", "stock", "unit_value")
        include_fk = True

    name = fields.String(required=True)
    unit_measure = fields.String(required=True)
    stock = fields.Integer(required=True)
    unit_value = fields.Decimal(places=2, required=True)

produto_schema = ProductSchema(many=True)