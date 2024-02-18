#!/usr/bin/python3

"""This module changes the name of a State object
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
    # change value of an attribute in a row based on the id
    record = session.query(State).where(State.id == 2).first()
    record.name = 'New Mexico'
    session.commit()

    session.close()
