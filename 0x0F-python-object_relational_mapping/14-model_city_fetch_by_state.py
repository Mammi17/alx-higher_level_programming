#!/usr/bin/python3
""" Python file similar to model_state.py named model_city.py
that contains the class definition of a City."""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    n = Session()
    res = n.query(City, State).\
        filter(City.state_id == State.id).all()
    for cty, ste in res:
        print("{}: ({}) {}".format(ste.name, cty.id, cty.name))
    n.commit()
    n.close()
