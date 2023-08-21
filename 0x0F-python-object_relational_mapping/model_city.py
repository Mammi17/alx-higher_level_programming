#!/usr/bin/python3
"""Create a new table with the class definition of City"""

from sys import argv
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """A new SQL table"""
    __tablename__ = "cities"
    id = Column("id", Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    nme = Column("name", String(128), nullable=False)
    ste_id = Column(Integer(), ForeignKey("states.id"), nullable=False)
