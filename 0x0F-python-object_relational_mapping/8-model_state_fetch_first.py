#!/usr/bin/python3

"""This module  prints the first State object
from the database hbtn_0e_6_usa

"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == '__main__':
    # getting db connection infirmations from CLA
    user, passwd, db = sys.argv[1:4]

    # creating a new engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, passwd, db),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # creating a new session object
    session = Session(engine)
    # querying the database for the first state in the states table
    record = session.query(State).order_by(State.id.asc()).first()

    if record:
        print("{}: {}".format(record.id, record.name))
    else:
        print()
