from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import db

class RegistrationModel(db.Model):
    __tablename__ = "registration"

    regi_id = db.Column("regi_id", Integer, primary_key=True, autoincrement=True)
    regi_dt = db.Column("regi_dt", DateTime, nullable=False)
    regi_tipe = db.Column("regi_tipe", Boolean, nullable=False)
    
    # foreign key
    fk_prod_id = db.Column("Produto.prod_id", Integer, ForeignKey("produto.prod_id"), ondelete="CASCADE")

    # relationship
    product = db.relationship("product", back_populates="registration")

    def __init__(self, regi_dt, regi_tipe, prod_id):
        self.regi_dt = regi_dt
        self.regi_tipe = regi_tipe
        self.prod_id = prod_id