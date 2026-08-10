from flask import Blueprint
from services import create_user, list_user, list_user_id, list_user_email, update_user, delete_user
from schemas import UserSchema

# create router
user_router = Blueprint("user", __name__)

# ROUTES
@user_router.post("/create")
def create_user_route(schema=UserSchema):
    return create_user(schema)

@user_router.get("/read")
def list_user_route():
    return list_user()

@user_router.get("/read_id")
def list_user_id_route(id):
    return list_user_id(id)

@user_router.get("/read_email")
def list_user_email_route(email):
    return list_user_email(email)

@user_router.put("/update")
def update_user_route(id, schema=UserSchema):
    return update_user(id, schema)

@user_router.delete("/delete")
def delete_user_route(id):
    return delete_user(id)