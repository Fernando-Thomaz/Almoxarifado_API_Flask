from src import ma
from marshmallow import fields
from src.models import ProductModel
from .category_schema import CategorySchema

class ProductSchema(ma.SQLAlchemyAutoSchema):
    # foreign key
    category = fields.Nested(
        CategorySchema,
        dump_only=True
    )

    class Meta:
        model = ProductModel
        load_instance = True
        fields = ("id", "name", "unit_measure", "stock", "unit_value")
        include_fk = True

    id = fields.Int(attribute="prod_id", dump_only=True)
    name = fields.String(attribute="prod_name", required=True)
    unit_measure = fields.String(attribute="prod_unit_measure", required=True)
    stock = fields.Integer(attribute="prod_stock", required=True)
    unit_value = fields.Decimal(attribute="prod_unit_value", places=2, required=True)

productschema = ProductSchema()
productsschema = ProductSchema(many=True)