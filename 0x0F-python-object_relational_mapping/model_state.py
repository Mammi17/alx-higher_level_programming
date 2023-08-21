#!/usr/bin/python3
"""a python file that contains the class definition of a State
and an instance Base = declarative_base()"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    ngne = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(ngne)
