#!/usr/bin/python3

"""This module prints all City objects
from the database hbtn_0e_14_usa

"""

import sys
from model_state import Base, State
from model_city import City
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

    # querying multiple tables using the join method
    records = session.query(State, City).join(City).order_by(
        City.id.asc()).all()
    for state, city in records:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
