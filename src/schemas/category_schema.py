from src import ma
from marshmallow import fields
from src.models import CategoryModel

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CategoryModel
        load_instance = True
        fields = ("id", "description")

    description = fields.String(required=True)

categoryschema = CategorySchema()
categoriesschema = CategorySchema(many=True)