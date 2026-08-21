from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from src.database.connection import db

class ProductModel(db.Model):
    __tablename__ = "product"

    prod_id = db.Column("prod_id", Integer, primary_key=True, autoincrement=True)
    prod_name = db.Column("prod_name", String(120), nullable=False)
    prod_unit_measure = db.Column("prod_unit_measure", String(120), nullable=False)
    prod_stock = db.Column("prod_stock", Integer, nullable=False)
    prod_unit_value = db.Column("prod_unit_value", Numeric(10,2), nullable=False)
    
    # foreign key
    fk_cate_id = db.Column("fk_cate_id", Integer, ForeignKey("category.cate_id", ondelete="CASCADE"))

    # relationship
    category = db.relationship("CategoryModel", back_populates="product")
    registration = db.relationship("RegistrationModel", back_populates="product", cascade="all, delete-orphan")