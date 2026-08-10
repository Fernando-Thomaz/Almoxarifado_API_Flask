from flask import Blueprint
from schemas import RegistrationSchema
from services import create_registration, list_registration, list_registration_type, list_registration_date, list_registration_product, update_registration, delete_registration

# create router
registration_router = Blueprint("registration", __name__)

# ROUTES
@registration_router.post("/create")
def create_registration_route(schema=RegistrationSchema):
    return create_registration(schema)

@registration_router.get("/read")
def list_registration_route():
    return list_registration()

@registration_router.get("/read_type")
def list_registration_type_route(type):
    return list_registration_type(type)

@registration_router.get("/read_date")
def list_registration_date_route(date):
    return list_registration_date(date)

@registration_router.get("/read_product_id")
def list_registration_product_route(product_id):
    return list_registration_product(product_id)

@registration_router.put("/update")
def update_registration_route(id, schema=RegistrationSchema):
    return update_registration(id, schema)

@registration_router.delete("/delete")
def delete_registration_route(id):
    return delete_registration(id)