from src import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from marshmallow import ValidationError
from src.schemas import productsschema, productschema
from src.services import create_product, list_product, list_product_category, list_product_name, update_product, delete_product

class ProductList(Resource):
    def get(self):
        """
        List all products
        ---
        tags:
          - Products
        responses:
          200:
            description: List all product
          404:
            description: Product doesnt exists
        """
        products = list_product()

        if not products:
            return make_response(jsonify({"message":"Products doesnt exists"}), 404)

        return productsschema.dump(products), 200

    def post(self):
        """
        Create product
        ---
        tags:
          - Products
        parameters:
          - in: body
            name: body
            required: True
            schema:
              type: object
              properties:
                name: 
                  type: string
                  example: example
                unit_measure:
                  type: string
                  example: meters
                stock:
                  type: integer
                  example: 10
                unit_value:
                  type: float
                  example: 10,2
        responses:
          201: 
            description: Create account
          409:
            description: Product already exist
          400:
            description: Error requisition
        """
        try:
            product = productschema.load(request.get_json())

        except ValidationError as err:
            return err.messages, 400

        if list_product_name(product["name"]):
            return {"message":"Product already exist"}, 409

        try:
            create = create_product(product)

            return productschema.dump(create), 201

        except Exception as e:
            return {"message":str(e)}, 400
api.add_resource(ProductList,"/products")

class ProductResource(Resource):
    def put(self, prod_id):
        """
        Update product
        ---
        tags:
          - Products
        parameters:
          - name: prod_id
            in: path
            type: integer
            required: True
          - in: body
            name: body
            required: True
            schema:
              type: object
              schema:
                name:
                  type: string
                  example: example
                unit_measure:
                  type: string
                  example: string
                stock:
                  type: integer
                  example: 10
                unit_value:
                  type: float
                  example: 10,2
        responses:
          200:
            description: Update product
          400:
            description: Error requisition
          404:
            description: Product not found
        """
        try:
            product = productschema.load(request.get_json)

        except ValidationError as err:
            return err.messages, 400

        new_product = update_product(
            prod_id,
           {"name":product.name,
            "unit_measure":product.unit_measure,
            "stock":product.stock,
            "unit_value":product.unit_value,
            "category":product.category}
        )

        if not new_product:
            return {"message":"Product not found"}, 404

        return productschema.dump(new_product), 200

    def delete(self, prod_id):
        """
        Product delete
        ---
        tags:
          - Products
        parameters:
          - name:
            in: path
            type: integer
            required: True
        responses:
          200: 
            description: Product delete success
          404:
            description: Product not found
        """
        if delete_product(prod_id):
            return {"message":"Product delete success"}, 200

        return {"message":"Product not found"}, 404
api.add_resource(ProductResource,"/products/<int:prod_id>")

class ProductResourceName(Resource):
    def get(self, prod_name):
        """
        Search product by name
        ---
        tags:
          - Products
        parameters:
          - name: prod_name
            in: path
            type: string
            required: True
        responses:
          200:
            description: Search product by name
          404:
            description: Product not found
        """
        product = list_product_name(prod_name)

        if not product:
            return {"message":"Product not found"}, 404

        return productschema.dump(product), 200 
api.add_resource(ProductResourceName,"/products/<string:prod_name>")

class ProductResourceCategory(Resource):
    def get(self, category):
        """
        Search product by category
        ---
        tags:
          - Products
        parameters:
          - name: fk_cate_id
            in: path
            type: integer
            required: True
        responses:
          200:
            description: Search product by category
          404:
            description: Product not found
        """
        product = list_product_category(category)

        if not product:
            return {"message":"Product not exist"}, 404

        return productschema.dump(product), 200
api.add_resource(ProductResourceCategory,"/products/<int:fk_cate_id>")