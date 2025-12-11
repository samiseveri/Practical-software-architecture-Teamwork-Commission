from typing import List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.store import Reduction
from app.schemas.reduction import ReductionCreate

class CRUDReduction(CRUDBase[Reduction, ReductionCreate, ReductionCreate]):
    def get_by_store(self, db: Session, store_id: int) -> List[Reduction]:
        return db.query(Reduction).filter(Reduction.store_user_id == store_id).all()
        
    def create_with_store(self, db: Session, obj_in: ReductionCreate, store_id: int):
        db_obj = Reduction(**obj_in.dict(), store_user_id=store_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

reduction = CRUDReduction(Reduction)
