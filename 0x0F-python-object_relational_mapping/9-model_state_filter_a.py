#!/usr/bin/python3
"""lists all State objects that contain the letter a from
the database hbtn_0e_6_usa"""

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
    for ste in n.query(State).\
            filter(State.name.like('%a%')).order_by(State.id).all():
        print("{}: {}".format(ste.id, ste.name))
    n.close()
