from typing import List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.product import PriceEntry
from app.schemas.price import PriceSubmission

class CRUDPrice(CRUDBase[PriceEntry, PriceSubmission, PriceSubmission]):
    def get_by_barcode(self, db: Session, barcode: str) -> List[PriceEntry]:
        return db.query(PriceEntry).filter(PriceEntry.barcode == barcode).all()

price_entry = CRUDPrice(PriceEntry)
