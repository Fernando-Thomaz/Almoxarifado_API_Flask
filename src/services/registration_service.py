from ..models import RegistrationModel
from ..database.connection import db

# CREATE
# function for create registration
def create_registration(registration):
    registration_db = RegistrationModel(regi_dt=registration.dt, regi_type=registration.type, prod_id=registration.product)

    db.session.add(registration_db)
    db.session.commit()
    return registration_db

# READ
# function for list registration
def list_registration():
    return RegistrationModel.session.query.all()

# function for list registration with date
def list_registration_date(registration):
    return RegistrationModel.session.query.filter_by(regi_dt=registration.dt).first()

# function for list registration with type
def list_registration_type(registration):
    return RegistrationModel.session.query.filter_by(regi_type=registration.type).first()

# function for list registration with product
def list_registration_product(registration):
    return RegistrationModel.session.query.filter_by(prod_id=registration.product).first()

# UPDATE
# function for update registration
def update_registration(id, new_registration):
    registration_db = RegistrationModel.session.get(id)

    if registration_db:
        registration_db.regi_dt = new_registration["dt"]
        registration_db.regi_type = new_registration["type"]

        db.session.commit()

        return registration_db

    return None

# DELETE
# function for delete registration
def delete_registration(id):
    registration_db = RegistrationModel.session.get(id)
    if registration_db:
        db.session.delete(registration_db)
        db.session.commit()

        return True

    return False