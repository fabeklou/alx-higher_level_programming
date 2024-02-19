#!/usr/bin/python3

"""This module deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa

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

    # delete a row from the states table
    records = session.query(State).filter(State.name.like('%a%')).all()
    for record in records:
        session.delete(record)
    session.commit()

    session.close()
