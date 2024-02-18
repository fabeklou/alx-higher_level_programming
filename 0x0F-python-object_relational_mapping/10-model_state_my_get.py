#!/usr/bin/python3

"""This module prints the State object with the name
passed as argument from the database hbtn_0e_6_usa

"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == '__main__':
    # getting db connection infirmations from CLA
    user, passwd, db, name = sys.argv[1:5]

    # creating a new engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, passwd, db),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # creating a new session object
    session = Session(engine)
    # querying the database
    record = session.query(State.id).where(State.name == name).first()

    if record:
        print(record.id)
    else:
        print('Not found')

    session.close()
