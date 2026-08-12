from marshmallow import ValidationError
from flask import request, make_response, jsonify
from flask_restful import Resource
from src import api
from services import create_registration, list_registration, list_registration_date, list_registration_type, list_registration_product, update_registration, delete_registration
from schemas import registrationsschema, registrationschema

class RegistrationList(Resource):
    def get(self):
        registrations = list_registration()

        if not registrations:
            return {"message":"Registrations doesn exist"}, 404

        return registrationsschema.dump(registrations), 200

    def post(self):
        try:
            registration = registrationschema.load(request.get_json())

        except ValidationError as err:
            return err.messages, 400

        try:
            create = create_registration(registration)

            return registrationschema.dump(create), 201

        except Exception as e:
            return {"message":str(e)}
api.add_resource(RegistrationList,"/registrations")

class RegistrationResource(Resource):
    def put(self, regi_id):
        try:
            registration = registrationschema.load(request.get_json())

        except ValidationError as err:
            return err.messages, 400

        new_registration = update_registration(
            regi_id,
            {"dt":registration.dt,
            "type":registration.type,
            "product":registration.product}
        )

        if not new_registration:
            return {"message":"Registration not found"}, 404

        return registrationschema.dump(new_registration), 200
         

    def delete(self, regi_id):
        if delete_registration(regi_id):
            return {"message":"Registration delete success"}, 200

        return {"message":"Registration not found"}, 404
api.add_resource(RegistrationResource,"/registration/<int:regi_id>")

class RegistrationResourceDate(Resource):
    def get(self, regi_dt):
            registration = list_registration_date(regi_dt)
    
            if not registration:
                return {"message":"Registration not found"}, 404
    
            return registrationschema.dump(registration), 200
api.add_resource(RegistrationResourceDate,"/registrations/<date:regi_dt>")

class RegistrationResourceType(Resource):
    def get(self, regi_type):
                registration = list_registration_type(regi_type)
        
                if not registration:
                    return {"message":"Registration not found"}, 404
        
                return registrationschema.dump(registration), 200
api.add_resource(RegistrationResourceType,"/registrations/<int:regi_type>")

class RegistrationResourceProduct(Resource):
    def get(self, prod_id):
                    registration = list_registration_product(prod_id)
            
                    if not registration:
                        return {"message":"Registration not found"}, 404
            
                    return registrationschema.dump(registration), 200
api.add_resource(RegistrationResourceProduct,"/registrations/<int:fk_prod_id>")