from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from src import api
from schemas import categoryschema, categoriesschema
from services import create_category, list_category, list_category_description, update_category, delete_category

class CategoryList(Resource):
    def get(self):
        categories = list_category()

        if not categories:
            return make_response(jsonify({"message":"categories doesnt exists"}), 404)

        return categoriesschema.dump(categories), 200

    def post(self):
        try:
            category = categoryschema.load(request.get_json())

        except ValidationError as err:
            return err.messages, 400

        if list_category_description(category["description"]):
            return {"message":"Category already exist"}, 409

        try:
            create = create_category(category)

            return categoryschema.dump(create), 201

        except Exception as e:
            return {"message":str(e)}, 400        
api.add_resource(CategoryList, "/categories")

class CategoryResource(Resource):
    def put(self, cate_id):
        try:
            category = categoryschema.load(request.get_json)

        except ValidationError as err:
            return err.messages, 400

        new_category = update_category(
            cate_id,
            {"description":category.description}
        )

        if not new_category:
            return {"message":"Category not found"}, 404

        return categoryschema.dump(new_category), 200

    def delete(self, cate_id):
        if delete_category(cate_id):
            return {"message":"Category delete success"}, 200

        return {"message":"Category not found"}, 404
api.add_resource(CategoryResource, "/categories/<int:cate_id>")