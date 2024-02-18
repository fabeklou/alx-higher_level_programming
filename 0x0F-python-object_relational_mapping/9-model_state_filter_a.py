#!/usr/bin/python3

"""This module lists all State objects that contain
the letter a from the database hbtn_0e_6_usa

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
    # querying the database
    records = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id.asc())

    for record in records:
        print("{}: {}".format(record.id, record.name))

    session.close()
