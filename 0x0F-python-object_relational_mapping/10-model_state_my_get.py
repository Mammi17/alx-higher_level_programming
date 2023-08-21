#!/usr/bin/python3
"""prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""

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
    ste = n.query(State).\
        filter(State.name == argv[4]).order_by(State.id).all()
    if ste:
        print("{}".format(ste[0].id))
    else:
        print("Not found")
    n.close()
