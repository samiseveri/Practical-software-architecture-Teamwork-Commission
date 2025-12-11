from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.base_class import Base

class Store(Base):
    # Just a helper model if we want strict store entities separate from Users
    # But per requirements, "Store Users" seem to represent stores.
    # We will use the User model for Store Users mostly.
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True, index=True)

class Reduction(Base):
    __tablename__ = "reductions"
    id = Column(Integer, primary_key=True, index=True)
    store_user_id = Column(Integer, ForeignKey("user.id"))
    product_barcode = Column(String, index=True)
    discount_percent = Column(Float)
    description = Column(String)
