from ..models import CategoryModel
from ..database.connection import db

# CREATE
# function for create category
def create_category(category):
    category_db = CategoryModel(cate_description=category.description)

    db.session.add(category_db)
    db.session.commit()
    return category_db

# READ
# function for list category
def list_category():
    return CategoryModel.query.all()

# UPDATE
# function for update category
def update_category(id, new_category):
    category_finder = CategoryModel.query.get(id)
    if category_finder:
        category_finder.cate_description = new_category["description"]

        db.session.commit()
        return new_category

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