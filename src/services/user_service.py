from ..models import UserModel
from ..database.connection import db

# CREATE
# function for create
def create_user(user):
    if not user.user_password:
        raise ValueError("Password is required")

    user.gen_password(user.user_password)

    db.session.add(user)
    db.session.commit()
    return user

# READ
# function for list
def list_user():
    return UserModel.query.all()

# function for list with id
def list_user_id(id):
    return UserModel.query.filter_by(user_id=id).first()

# function for list with email
def list_user_email(email):
    return UserModel.query.filter_by(user_email=email).first()

# function for list with name
def list_user_name(name):
    return UserModel.query.filter_by(user_name=name).first()

# UPDATE
# function for update user
def update_user(id, user):
    user_finder = UserModel.query.get(id)
    if user_finder:
        user_finder.user_name = user.user_name
        user_finder.user_email = user.user_email

        if user != "":
            user_finder.gen_password(user.user_password)

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