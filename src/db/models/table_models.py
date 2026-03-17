import os
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base

SCHEMA = os.getenv('data', 'POSTGRES_SCHEMA')

class Papers(Base):
    __tablename__ = 'papers'
    __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    author = Column(Text, nullable=False)
    journal = Column(Text, nullable=False)
    doi = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Coatings(Base):
    __tablename__ = 'coatings'
    __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True, index=True)
    coating = Column(Text, nullable=False)
    elements = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

