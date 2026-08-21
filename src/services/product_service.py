from ..models import ProductModel
from ..database.connection import db

# CREATE
# function for create product
def create_product(product):
    db.session.add(product)
    db.session.commit()
    return product

# READ
# function for list product
def list_product():
    return ProductModel.query.all()

# function for list product with name
def list_product_name(name):
    return ProductModel.query.filter_by(prod_name=name).first()

# function for list product with category
def list_product_category(category_id):
    return ProductModel.query.filter_by(fk_cate_id=category_id).first()

# UPDATE
# function for update category
def update_product(id, product):
    product_db = ProductModel.query.get(id)
    if product_db:
        product_db.prod_name = product.prod_name
        product_db.prod_unit_measure = product.prod_unit_measure
        product_db.prod_stock = product.prod_stock
        product_db.prod_unit_value = product.prod_unit_value
        product_db.fk_cate_id = product.fk_cate_id

        db.session.commit()
        return product_db

    return None

# DELETE
# function for delete product
def delete_product(id):
    product_db = ProductModel.query.get(id)
    if product_db:
        db.session.delete(product_db)
        db.session.commit()
        return True

    return False