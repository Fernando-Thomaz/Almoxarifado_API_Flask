from marshmallow import ValidationError
from flask import request, make_response, jsonify
from flask_restful import Resource
from src import api
from src.services import create_registration, list_registration, list_registration_date, list_registration_type, list_registration_product, update_registration, delete_registration
from src.schemas import registrationsschema, registrationschema

class RegistrationList(Resource):
    def get(self):
        """
        List all registrations
        ---
        tags:
          - Registrations
        responses:
          200:
            description: List all registrations
          404:
            description: Registration doesnt exists
        """
        registrations = list_registration()

        if not registrations:
            return make_response(jsonify({"message":"Registration doesnt exists"}), 404)

        return registrationsschema.dump(registrations), 200

    def post(self):
        """
        Create registration
        ---
        tags:
          - Registrations
        parameters:
          - in: body
            name: body
            required: True
            schema:
              type: object
              properties:
                dt:
                  type: string
                  format: date-time
                  example: "2026-08-19T11:20:00Z"
                type:
                  type: boolean
                  example: 1
                product:
                  type: integer
                  example: 1
        responses:
          201:
            description: Registration create
          400:
            description: Error requisition
        """
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
        """
        Update registration
        ---
        tags:
          - Registrations
        parameters:
          - name: regi_id
            in: path
            type: integer
            required: True
          - in: body
            name: body
            required: True
            schema:
              type: object
              properties:
                dt:
                  type: string
                  format: date-time
                  example: "2026-08-19T11:30:00Z"
                type:
                  type: boolean
                  example: 1
                product:
                  type: integer
                  example: 10
        responses:
          200:
            description: Update registration success
          404:
            description: Registration not found
        """
        try:
            registration = registrationschema.load(request.get_json())

        except ValidationError as err:
            return err.messages, 400

        new_registration = update_registration(regi_id, registration)

        if not new_registration:
            return {"message":"Registration not found"}, 404

        return registrationschema.dump(new_registration), 200
         

    def delete(self, regi_id):
        """
        Delete registration
        ---
        tags:
          - Registrations
        parameters:
          - name: regi_id
            in: path
            type: integer
            required: True
        responses:
          200:
            description: Registration delete success
          404:
            description: Registration not found
        """
        if delete_registration(regi_id):
            return {"message":"Registration delete success"}, 200

        return {"message":"Registration not found"}, 404
api.add_resource(RegistrationResource,"/registration/<int:regi_id>")

class RegistrationResourceDate(Resource):
    def get(self, regi_dt):
      """
      Search registration by date
      ---
      tags:
        - Registrations
      parameters:
        - name: regi_dt
          in: path
          type: string
          format: date
          required: True
      responses:
        200:
          description: Search registration by date
        404:
          description: Registration not found
      """
      registration = list_registration_date(regi_dt)

      if not registration:
          return {"message":"Registration not found"}, 404

      return registrationschema.dump(registration), 200
api.add_resource(RegistrationResourceDate,"/registrations/<string:regi_dt>")

class RegistrationResourceType(Resource):
    def get(self, regi_type):
      """
      Search registration by type
      ---
      tags:
        - Registrations
      parameters:
        - name: regi_type
          in: path
          type: boolean
          required: True
      responses:
        200:
          description: Search registration by date
        404:
          description: Registration not found
      """
      registration = list_registration_type(regi_type)

      if not registration:
          return {"message":"Registration not found"}, 404

      return registrationschema.dump(registration), 200
api.add_resource(RegistrationResourceType,"/registrations/<int:regi_type>")

class RegistrationResourceProduct(Resource):
    def get(self, prod_id):
      """
      Search registration by product
      ---
      tags:
        - Registrations
      parameters:
        - name: prod_id
          in: path
          type: integer
          required: True
      responses:
        200:
          description: Search registration by product
        404:
          description: Registration not found
      """
      registration = list_registration_product(prod_id)

      if not registration:
          return {"message":"Registration not found"}, 404

      return registrationschema.dump(registration), 200
api.add_resource(RegistrationResourceProduct,"/registrations/<int:fk_prod_id>")