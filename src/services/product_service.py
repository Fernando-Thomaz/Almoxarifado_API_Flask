from ..models import ProductModel
from ..database.connection import db

# CREATE
# function for create product
def create_product(product):
    product_db = ProductModel(prod_name=product.name, prod_unit_measure=product.unit_measure, prod_stock=product.stock, prod_unit_value=product.unit_value, cate_id=product.category)

    db.session.add(product_db)
    db.session.commit()
    return product_db

# READ
# function for list product
def list_product():
    return ProductModel.session.query.all()

# function for list product with name
def list_product_name(name):
    return ProductModel.session.query.filter_by(prod_name=name).first()

# function for list product with category
def list_product_category(category_id):
    return ProductModel.session.query.filter_by(fk_cate_id=category_id).first()

# UPDATE
# function for update category
def update_category(id, new_category):
    product_db = ProductModel.session.get(id)
    if product_db:
        product_db.prod_name = new_category["name"]
        product_db.prod_unit_measure = new_category["unit_measure"]
        product_db.prod_stock = new_category["stock"]
        product_db.unit_value = new_category["unit_value"]

        product_db.fk_cate_id = new_category["category"]

        db.session.commit()
        return product_db

    return None

# DELETE
# function for delete product
def delete_product(id):
    product_db = ProductModel.session.get(id)
    if product_db:
        db.session.delete(product_db)
        db.session.commit()
        return True

    return False