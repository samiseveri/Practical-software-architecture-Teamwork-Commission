from sqlalchemy import Boolean, Column, Integer, String, Enum
from app.db.base_class import Base
import enum

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    STORE_USER = "store_user"

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default=UserRole.STORE_USER)
    
    # Store User specific fields
    is_active = Column(Boolean, default=False) # Must be activated by Admin
    is_locked = Column(Boolean, default=False) # Can be locked by Admin
    store_name = Column(String, nullable=True) # For store users
    
    # Simplified Location for store users (stored as generic float for simplicity)
    latitude = Column(String, nullable=True) 
    longitude = Column(String, nullable=True)
