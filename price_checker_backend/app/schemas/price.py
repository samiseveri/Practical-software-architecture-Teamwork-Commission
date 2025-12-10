from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class PriceSubmission(BaseModel):
    barcode: str
    barcode_type: str
    price: float
    latitude: float
    longitude: float
    timestamp: Optional[datetime] = None

class PriceResponse(BaseModel):
    store_name: str
    price: float
    label: str  # e.g., "Expensive", "Inexpensive"
    distance_km: Optional[float] = None

class PriceBatch(BaseModel):
    items: List[PriceSubmission]
