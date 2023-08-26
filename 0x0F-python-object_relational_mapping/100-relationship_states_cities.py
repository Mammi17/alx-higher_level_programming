#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    ngne = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2],
            argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(ngne)
    Session = sessionmaker(bind=ngne)
    n = Session()
    n_ste = State(name="California")
    n.add(n_ste)
    n.commit()
    n_cty = City(name="San Francisco", state_id=n_ste.id)
    n.add(n_cty)
    n.commit()
    n.close()
