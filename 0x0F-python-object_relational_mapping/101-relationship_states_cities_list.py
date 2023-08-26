#!/usr/bin/python3
"""lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    ngne = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=ngne)
    n = Session()
    for ste in n.query(State).order_by(State.id):
        print("{}: {}".format(ste.id, ste.name))
        for cty in ste.cities:
            print("\t{}: {}".format(cty.id, cty.name))
