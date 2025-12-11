from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime

class PriceEntry(Base):
    __tablename__ = "price_entries"

    id = Column(Integer, primary_key=True, index=True)
    barcode = Column(String, index=True)
    barcode_type = Column(String)
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    # Location data where scan happened
    latitude = Column(Float)
    longitude = Column(Float)
    
    # If this price comes from a specific store (Store User)
    store_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    
    # Justification: Storing denormalized location for shoppers to enable quick geospatial queries without joins
