from ..models import UserModel
from ..database.connection import db

# CREATE
# function for create
def create_user(user):
    user_db = UserModel(user_name=user.name, user_email=user.email, user_password=user.password)
    user_db.gen_password(user.password)

    db.session.add(user_db)
    db.session.commit()
    return user_db

# READ
# function for list
def list_user():
    return UserModel.query.all()

# function for list with id
def list_user_id(id):
    return UserModel.session.query.filter_by(user_id=id).first()

# function for list with email
def list_user_email(email):
    return UserModel.session.query.filter_by(user_email=email).first()

# function for list with name
def list_user_name(name):
    return UserModel.session.query.filter_by(user_name=name).first()

# UPDATE
# function for update user
def update_user(id, new_user):
    user_finder = UserModel.query.get(id)
    if user_finder:
        user_finder.name = new_user["name"]
        user_finder.email = new_user["email"]

        if new_user.get("password"):
            user_finder.gen_password(new_user["password"])

        db.session.commit()
        return user_finder

    return None

# DELETE
# function for delete user
def delete_user(id):
    user_finder = UserModel.query.get(id)
    if user_finder:
        db.session.delete(user_finder)
        db.session.commit()
        return True

    return False