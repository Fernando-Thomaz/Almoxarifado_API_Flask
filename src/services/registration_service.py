from ..models import RegistrationModel
from ..database.connection import db

# CREATE
# function for create registration
def create_registration(registration):
    db.session.add(registration)
    db.session.commit()
    return registration

# READ
# function for list registration
def list_registration():
    return RegistrationModel.query.all()

# function for list registration with date
def list_registration_date(dt):
    return RegistrationModel.query.filter_by(regi_dt=dt).first()

# function for list registration with type
def list_registration_type(type):
    return RegistrationModel.query.filter_by(regi_type=type).first()

# function for list registration with product
def list_registration_product(product):
    return RegistrationModel.query.filter_by(fk_prod_id=product).first()

# UPDATE
# function for update registration
def update_registration(id, registration):
    registration_db = RegistrationModel.query.get(id)

    if registration_db:
        registration_db.regi_dt = registration.regi_dt
        registration_db.regi_type = registration.regi_type
        registration_db.fk_prod_id = registration.fk_prod_id

        db.session.commit()

        return registration_db

    return None

# DELETE
# function for delete registration
def delete_registration(id):
    registration_db = RegistrationModel.query.get(id)
    if registration_db:
        db.session.delete(registration_db)
        db.session.commit()

        return True

    return False