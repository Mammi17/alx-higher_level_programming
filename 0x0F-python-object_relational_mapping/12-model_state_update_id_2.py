#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    ngne = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(ngne)
    Session = sessionmaker(bind=ngne)
    n = Session()
    ste = n.query(State).filter(State.id == 2).all()
    if ste:
        ste[0].name = "New Mexico"
    n.commit()
    n.close()
