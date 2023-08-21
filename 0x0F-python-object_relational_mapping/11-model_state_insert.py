#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

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
    n_ste = State(name="Louisiana")
    n.add(n_ste)
    n.commit()
    print(n_ste.id)
    n.close()
