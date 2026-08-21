from ..models import CategoryModel
from ..database.connection import db

# CREATE
# function for create category
def create_category(category):
    db.session.add(category)
    db.session.commit()
    return category

# READ
# function for list category
def list_category():
    return CategoryModel.query.all()

# function for list category with description
def list_category_description(description):
    return CategoryModel.query.filter_by(cate_description=description).first()

# UPDATE
# function for update category
def update_category(id, category):
    category_finder = CategoryModel.query.get(id)
    if category_finder:
        category_finder.cate_description = category.cate_description

        db.session.commit()
        return category_finder

    return None

# DELETE
# function for delete category
def delete_category(id):
    category_finder = CategoryModel.query.get(id)
    if category_finder:
        db.session.delete(category_finder)
        db.session.commit()
        return True

    return False