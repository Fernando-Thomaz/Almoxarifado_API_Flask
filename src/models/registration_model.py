from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database.connection import db

class RegistrationModel(db.Model):
    __tablename__ = "registration"

    regi_id = db.Column("regi_id", Integer, primary_key=True, autoincrement=True)
    regi_dt = db.Column("regi_dt", DateTime, nullable=False)
    regi_type = db.Column("regi_type", Boolean, nullable=False)
    
    # foreign key
    fk_prod_id = db.Column("fk_prod_id", Integer, ForeignKey("product.prod_id", ondelete="CASCADE"))

    # relationship
    product = db.relationship("ProductModel", back_populates="registration")

    def __init__(self, regi_dt, regi_type, prod_id):
        self.regi_dt = regi_dt
        self.regi_type = regi_type
        self.prod_id = prod_id