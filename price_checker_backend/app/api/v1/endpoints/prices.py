from typing import Any, List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.api import deps
from app.crud.crud_price import price_entry
from app.schemas.price import PriceSubmission, PriceResponse
from app.services.labeling_strategy import label_price
from app.services.location_service import calculate_distance

router = APIRouter()

@router.post("/", response_model=PriceSubmission)
def submit_price(
    *,
    db: Session = Depends(deps.get_db),
    price_in: PriceSubmission,
) -> Any:
    # Save the raw data
    price_entry.create(db, obj_in=price_in)
    return price_in

@router.get("/compare", response_model=List[PriceResponse])
def compare_prices(
    *,
    db: Session = Depends(deps.get_db),
    barcode: str,
    lat: float,
    lon: float,
    max_distance_km: float = 10.0,
) -> Any:
    # 1. Fetch all entries for this barcode
    # In a real heavy-load scenario, we would use PostGIS or filtered queries.
    # For this assignment's scale, fetching and filtering in Python is acceptable (KISS).
    all_prices = price_entry.get_by_barcode(db, barcode=barcode)
    
    # 2. Filter by distance
    nearby_prices = []
    prices_values = []
    
    for entry in all_prices:
        if entry.latitude and entry.longitude:
            dist = calculate_distance(lat, lon, entry.latitude, entry.longitude)
            if dist <= max_distance_km:
                # If store_id exists, try to get store name, else use "Unknown Location"
                store_name = "Unknown Store" # Logic to fetch store name from user table would go here
                
                nearby_prices.append({
                    "store_name": store_name,
                    "price": entry.price,
                    "distance_km": dist
                })
                prices_values.append(entry.price)
    
    # 3. Labeling Logic
    results = []
    for item in nearby_prices:
        label = label_price(item["price"], prices_values)
        results.append(PriceResponse(
            store_name=item["store_name"],
            price=item["price"],
            label=label,
            distance_km=item["distance_km"]
        ))
        
    # 4. Sort by price
    results.sort(key=lambda x: x.price)
    
    return results
