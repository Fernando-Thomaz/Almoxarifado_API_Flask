from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from src import api
from src.schemas import categoryschema, categoriesschema
from src.services import create_category, list_category, list_category_description, update_category, delete_category

class CategoryList(Resource):
    def get(self):
        """
        List all categories
        ---
        tags:
          - Categories
        responses:
          200:
            description: List all categories
          404:
            description: Categories doesnt exists
        """
        categories = list_category()

        if not categories:
            return make_response(jsonify({"message":"categories doesnt exists"}), 404)

        return categoriesschema.dump(categories), 200

    def post(self):
        """
        Create category
        ---
        tags:
          - Categories
        parameters:
          - in: body
            name: body
            required: True
            schema:
              type: object
              properties:
                description: 
                  type: string
                  example: example
        responses:
          201:
            description: Create category
          409:
            description: Category already exist
          400:
            description: Error requisition
        """
        try:
            category = categoryschema.load(request.get_json())

        except ValidationError as err:
            return err.messages, 400

        if list_category_description(category.cate_description):
            return {"message":"Category already exist"}, 409

        try:
            create = create_category(category)

            return categoryschema.dump(create), 201

        except Exception as e:
            return {"message":str(e)}, 400        
api.add_resource(CategoryList, "/categories")

class CategoryResource(Resource):
    def put(self, cate_id):
        """
        Update category
        ---
        tags:
          - Categories
        parameters:
          - name: cate_id
            in: path
            type: integer
            required: True
          - in: body
            name: body
            required: True
            schema:
              type: object
              properties:
                description:
                  type: string
                  example: example
        responses:
          200:
            description: Category update success
          404:
            description: Category not found
        """
        try:
            category = categoryschema.load(request.get_json())

        except ValidationError as err:
            return err.messages, 400

        new_category = update_category(cate_id, category)

        if not new_category:
            return {"message":"Category not found"}, 404

        return categoryschema.dump(new_category), 200

    def delete(self, cate_id):
        """
        Delete category
        ---
        tags:
          - Categories
        parameters:
          - name: cate_id
            in: path
            type: integer
            required: True
        responses:
          200:
            description: Category delete success
          404:
            description: Category not found
        """
        if delete_category(cate_id):
            return {"message":"Category delete success"}, 200

        return {"message":"Category not found"}, 404
api.add_resource(CategoryResource, "/categories/<int:cate_id>")