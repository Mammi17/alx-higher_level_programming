#!/usr/bin/python3
"""a python file that contains the class definition of a State
and an instance Base = declarative_base()"""

from sys import argv
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """A new SQL table"""
    __tablename__ = "states"
    id = Column("id", Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    nme = Column("name", String(128), nullable=False)
