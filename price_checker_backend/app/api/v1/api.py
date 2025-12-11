from fastapi import APIRouter
from app.api.v1.endpoints import login, users, prices, stores

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(prices.router, prefix="/prices", tags=["prices"])
api_router.include_router(stores.router, prefix="/stores", tags=["stores"])
