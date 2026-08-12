from schemas import usersschema, userschema
from services import create_user, list_user, list_user_id, list_user_email, list_user_name, update_user, delete_user
from flask_restful import Resource
from flask import request, jsonify, make_response
from src import api
from marshmallow import ValidationError

class UserList(Resource):
    def get(self):
        users = list_user()

        if not users:
            return make_response(jsonify({"message": "Users doesnt exists"}), 404)

        return make_response(jsonify(usersschema.dump(users)), 200)

    def post(self):
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
        user = list_user_id(user_id)

        if not user:
            return {"message":"User doesnt exist"}, 404

        return userschema.dump(user), 200

    def put(self, user_id):
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
        if delete_user(user_id):
            return {"message":"User delete success"}, 200

        return {"message":"User not found"}, 404
api.add_resource(UserResource, "/users/<int:user_id>")

class UserResourceEmail(Resource):
    def get(self, user_email):
        user = list_user_email(user_email)

        if not user:
            return {"message":"User not found"}, 404

        return userschema.dump(user), 200
api.add_resource(UserResourceEmail, "/users/<str:user_email>")

class UserResourceName(Resource):
    def get(self, user_name):
        user = list_user_name(user_name)

        if not user:
            return {"message":"User not found"}, 404

        return userschema.dump(user), 200
api.add_resource(UserResourceName, "/users/<str:user_name>")