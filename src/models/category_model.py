from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database.connection import db

class Category(db.Model):
    __tablename__ = "category"

    cate_id = db.Column("cate_id", Integer, primary_key=True, autoincrement=True)
    cate_description = db.Column("cate_description", String(120), nullable=False)

    #relationship
    product = db.relationship("product", back_populates="category", cascade="all, delete-orphan")

    def __init__(self, cate_description):
        self.cate_description = cate_description