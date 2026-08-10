from flask import Blueprint
from schemas import ProductSchema
from services import create_product, list_product, list_product_name, list_product_category, update_product, delete_product

# create router
product_router = Blueprint("product", __name__)

# ROUTE
@product_router.post("/create")
def create_product_route(schema=ProductSchema):
    return create_product(schema)

@product_router.get("/read")
def list_product_route():
    return list_product()

@product_router.get("/read_name")
def list_product_name_route(name):
    return list_product_name(name)

@product_router.get("/read_category_id")
def list_product_category_route(category_id):
    return list_product_category(category_id)

@product_router.put("/update")
def update_product_route(id, schema=ProductSchema):
    return update_product(id, schema)

@product_router.delete("/delete")
def delete_product_route(id):
    return delete_product(id)