from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class Papers(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    author = Column(Text, nullable=False)
    journal = Column(Text, snullable=False)
    doi = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # tools = relationship("Tool", back_populates="coating")