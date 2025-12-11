from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    store_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class UserUpdate(BaseModel):
    is_active: Optional[bool] = None
    is_locked: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    role: str
    is_active: bool
    is_locked: bool
    store_name: Optional[str] = None

    class Config:
        from_attributes = True
