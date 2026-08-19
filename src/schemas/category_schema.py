from src import ma
from marshmallow import fields
from src.models import CategoryModel

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CategoryModel
        load_instance = True
        fields = ("id", "description")

    id = fields.Int(attribute="cate_id", dump_only=True)
    description = fields.String(attribute="cate_description", required=True)

categoryschema = CategorySchema()
categoriesschema = CategorySchema(many=True)