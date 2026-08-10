from flask import Blueprint
from schemas import CategorySchema
from services import create_category, list_category, update_category, delete_category

# create router
category_router = Blueprint("category", __name__)

# ROUTES
@category_router.post("/create")
def create_category_route(schema=CategorySchema):
    return create_category(schema)

@category_router.get("/read")
def list_category_route():
    return list_category()

@category_router.put("/update")
def update_category_route(schema=CategorySchema):
    return update_category(id, schema)

@category_router.delete("/delete")
def delete_category_route(id):
    return delete_category(id)