from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.crud.crud_reduction import reduction
from app.schemas.reduction import ReductionCreate, ReductionResponse
from app.schemas.price import PriceBatch
from app.crud.crud_price import price_entry
from app.models.user import User

router = APIRouter()

@router.post("/reductions", response_model=ReductionResponse)
def add_reduction(
    *,
    db: Session = Depends(deps.get_db),
    reduction_in: ReductionCreate,
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create a new reduction entry for a store user.
    - Only users with the role `store_user` are allowed
    - The reduction is automatically associated with the current store
    """
    if current_user.role != "store_user":
         raise HTTPException(status_code=400, detail="Only store users can add reductions")
    
    item = reduction.create_with_store(db, obj_in=reduction_in, store_id=current_user.id)
    return item

@router.post("/batch-upload")
def batch_upload_prices(
    *,
    db: Session = Depends(deps.get_db),
    batch: PriceBatch,
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    # Ensures that only store users can upload batches
    if current_user.role != "store_user":
         raise HTTPException(status_code=400, detail="Only store users can upload batches")
         
    count = 0
    for item in batch.items:
        # We enforce the store's location if they are a fixed store user
        if current_user.latitude and current_user.longitude:
            item.latitude = float(current_user.latitude)
            item.longitude = float(current_user.longitude)
        #Creates price entry in the database
        price_entry.create(db, obj_in=item)
        count += 1
    return {"message": f"Successfully processed {count} items"}
