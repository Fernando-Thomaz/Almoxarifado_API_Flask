from src.schemas import usersschema, userschema
from src.services import create_user, list_user, list_user_id, list_user_email, list_user_name, update_user, delete_user
from flask_restful import Resource
from flask import request, jsonify, make_response
from src import api
from marshmallow import ValidationError

class UserList(Resource):
    def get(self):
        """
        List all users
        ---
        tags:
          - Users
        responses:
          200:
            description: List all users
          404:
            description: User not found
        """
        users = list_user()

        if not users:
            return make_response(jsonify({"message": "Users doesnt exists"}), 404)

        return make_response(jsonify(usersschema.dump(users)), 200)

    def post(self):
        """
        Create user
        ---
        tags:
          - Users
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
                email:
                  type: string
                  example: example@gmail.com
                password:
                  type: string
                  example: example
        responses:
          201:
            description: Create account success
          409:
            description: Email already exist
          400:
            description: Error requisition
        """
        try:
            user = userschema.load(request.get_json())
            
        except ValidationError as err:
            return err.messages, 400

        if list_user_email(user.email):
            return {"message":"Email already exist"}, 409

        try:
            create = create_user(user)

            return userschema.dump(create), 201

        except Exception as e:
            return {"message":str(e)}, 400
api.add_resource(UserList, "/users")

class UserResource(Resource):
    def get(self, user_id):
        """
        Search user by id
        ---
        tags:
          - Users
        parameters:
          - name: user_id
            in: path
            type: integer
            required: True
        responses:
          200:
            description: List users
          404:
            description: User not found
          400:
            description: Error requisition
        """
        user = list_user_id(user_id)

        if not user:
            return {"message":"User doesnt exist"}, 404

        return userschema.dump(user), 200

    def put(self, user_id):
        """
        Update user
        ---
        tags:
          - Users
        parameters:
          - name: user_id
            in: path
            type: integer
            required: True
          - in: body
            name: body
            required: True
            schema:
              type: object
              properties:
                name:
                  type: string
                  example: example
                email:
                  type: string
                  example: example@gmail.com
                password:
                  type: string
                  example: example
        responses:
          200:
            description: Update success
          404:
            description: User not found
        """
        try:
            user = userschema.load(request.get_json())

        except ValidationError as err:
            return err.messages, 400

        new_user = update_user(
            user_id, 
            {"name":user.name,
             "email":user.email,
             "password":user.password}
        )

        if not new_user:
            return {"message":"User not found"}, 404

        return userschema.dump(new_user), 200

    def delete(self, user_id):
        """
        Delete user
        ---
        tags:
          - Users
        parameters:
          - name: user_id
            in: path
            type: integer
            required: True
        responses:
          200: 
            description: Delete user success
          404:
            description: User not found
        """
        if delete_user(user_id):
            return {"message":"User delete success"}, 200

        return {"message":"User not found"}, 404
api.add_resource(UserResource, "/users/<int:user_id>")

class UserResourceEmail(Resource):
    def get(self, user_email):
        """
        Search user by email
        ---
        tags:
          - Users
        parameters:
          - name: user_email
            in: path
            type: integer
            required: True
        responses:
          200:
            description: List user
          404:
            description: User not found
        """
        user = list_user_email(user_email)

        if not user:
            return {"message":"User not found"}, 404

        return userschema.dump(user), 200
api.add_resource(UserResourceEmail, "/users/<string:user_email>")

class UserResourceName(Resource):
    def get(self, user_name):
        """
        Search by name
        ---
        tags:
          - Users
        parameters:
          - name: user_name
            in: path
            type: string
            required: True
        responses:
          200: 
            description: List user
          404:
            description: User not found
        """
        user = list_user_name(user_name)

        if not user:
            return {"message":"User not found"}, 404

        return userschema.dump(user), 200
api.add_resource(UserResourceName, "/users/<string:user_name>")