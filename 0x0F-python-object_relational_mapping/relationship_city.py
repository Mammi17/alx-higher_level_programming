#!/usr/bin/python3
"""Lists states"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

class City(Base):
    """Class representing the states table"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    nme = Column(String(128), nullable=False)
    ste_id = Column(Integer, ForeignKey("states.id"), nullable=False)
