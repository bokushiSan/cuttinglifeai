from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class Coatings(Base):
    __tablename__ = "coatings"

    id = Column(Integer, primary_key=True, index=True)
    coating = Column(Text, nullable=False)
    elements = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

