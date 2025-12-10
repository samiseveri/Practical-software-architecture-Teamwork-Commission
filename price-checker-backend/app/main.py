from fastapi import FastAPI
from app.api.v1 import admin_routes, store_user_routes, price_routes

app = FastAPI(title="Price Checker Backend")

app.include_router(admin_routes.router, prefix="/api/v1/admin", tags=["Admin"])
app.include_router(store_user_routes.router, prefix="/api/v1/store-users", tags=["Store Users"])
app.include_router(price_routes.router, prefix="/api/v1/prices", tags=["Prices"])

@app.get("/")
def health_check():
    return {"status": "running"}
