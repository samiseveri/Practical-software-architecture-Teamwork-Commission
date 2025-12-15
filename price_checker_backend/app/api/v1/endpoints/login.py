from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.api import deps
from app.core import security
from app.crud.crud_user import user as crud_user
from app.schemas.token import Token

router = APIRouter()
# Endpoint for user login and JWT token generation
# Database session is injected via dependency
# OAuth2PasswordRequestForm is used to parse login form data
@router.post("/login/access-token", response_model=Token)
def login_access_token(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = crud_user.get_by_email(db, email=form_data.username)
    # Validates user existence and password corectness
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    # Ensures the user account is active, approved by admin
    if not user.is_active:
        raise HTTPException(status_code=400, detail="User is not active. Please wait for Admin approval.")
    # Prevents login if the account is locked
    if user.is_locked:
        raise HTTPException(status_code=400, detail="User account is locked.")
    # Defines access token expiration time    
    access_token_expires = timedelta(minutes=security.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    # Generates and returns the JWT access token
    return {
        "access_token": security.create_access_token(user.email, expires_delta=access_token_expires),
        "token_type": "bearer",
    }
