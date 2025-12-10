from pydantic import BaseModel

class ReductionCreate(BaseModel):
    product_barcode: str
    discount_percent: float
    description: str

class ReductionResponse(ReductionCreate):
    id: int
    store_user_id: int
    
    class Config:
        from_attributes = True
